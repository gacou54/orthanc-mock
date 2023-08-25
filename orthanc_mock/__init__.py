try:
    from orthanc import *

except ModuleNotFoundError:
    from .orthanc_mock import *
