# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""screenplay-writer-agent - A Bindu Agent."""

from screenplay_writer_agent.__version__ import __version__
from screenplay_writer_agent.main import (
    handler,
    initialize_crew,
    cleanup,
    main,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_crew",
    "cleanup",
    "main",
]