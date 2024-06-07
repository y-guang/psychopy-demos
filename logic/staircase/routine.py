"""
Note: Psychopy has built-in staircase procedures, check that before determine if this is needed.
"""


from typing import Generic, TypeVar, List, Callable, Optional

T = TypeVar('T')


class StairCase(Generic[T]):
    """
    A staircase procedure that based on each response to adjust the current testing value, 
    and record the results.
    """

    def __init__(self,
                 start: T,
                 n_correct: int,
                 n_wrong: int,
                 n_reversals: int,
                 func_correct: Callable[[T], T],
                 func_wrong: Callable[[T], T],) -> None:
        """
        :param start: the initial value
        :param n_correct: the number of correct responses required to adjust the current value
        :param n_wrong: the number of wrong responses required to adjust the current value
        :param n_reversals: the number of reversals required to finish the test
        :param func_correct: a function to adjust the current value when the response is correct
        :param func_wrong: a function to adjust the current value when the response is wrong
        """
        super().__init__()
        # config
        self.start = start
        self.n_correct = n_correct
        self.n_wrong = n_wrong
        self.n_reversals = n_reversals
        self.func_correct = func_correct
        self.func_wrong = func_wrong

        # status
        self.current = start
        self.toward_correct: Optional[bool] = None
        self.correct_count = 0
        self.wrong_count = 0
        self.values: List[T] = []
        self.correctness: List[bool] = []
        self.turning_points: List[T] = []

    def correct(self):
        """
        Record a correct response and adjust the current value if necessary.
        """
        self.values.append(self.current)
        self.correctness.append(True)
        self.correct_count += 1
        if self.correct_count >= self.n_correct:
            self.correct_count = 0
            self.wrong_count = 0
            # turning point or not
            if self.toward_correct is None:
                self.toward_correct = True
            elif not self.toward_correct:
                # a turning point
                self.turning_points.append(self.current)
                self.toward_correct = True
            else:
                pass
            # next value
            self.current = self.func_correct(self.current)

    def wrong(self):
        """
        Record a wrong response and adjust the current value if necessary.
        """
        self.values.append(self.current)
        self.correctness.append(False)
        self.wrong_count += 1
        if self.wrong_count >= self.n_wrong:
            self.correct_count = 0
            self.wrong_count = 0
            # turning point or not
            if self.toward_correct is None:
                self.toward_correct = False
            elif self.toward_correct:
                # a turning point
                self.turning_points.append(self.current)
                self.toward_correct = False
            else:
                pass
            # next value
            self.current = self.func_wrong(self.current)

    def is_stopped(self) -> bool:
        """
        Check if the test procedure is stopped.
        """
        return len(self.turning_points) >= self.n_reversals
