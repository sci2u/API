import plotting
from core import generator
from quiz import QuizQuestionBase, QuizAnswerBase
from puzzle import PuzzleQuestionBase, PuzzleAnswerBase, PuzzleTileBase
from helpers import latex, latex_matrix


plotting.matplotlib_init()
plotting.matplotlib_enable_latex()

# Legacy
QuestionBase = QuizQuestionBase
AnswerBase = QuizAnswerBase
