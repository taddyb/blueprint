import logging
from pathlib import Path
from typing import Any, Dict
from typing_extensions import Annotated

from pydantic import (
    BaseModel,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
)
from pydantic.functional_validators import WrapValidator

log = logging.getLogger(__name__)


def maybe_has_path(
    v: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
) -> Path:
    """
    Custom validator function to check if the provided value is a valid Path.

    Parameters
    ----------
    v : Any
        The value to be validated.
    handler : ValidatorFunctionWrapHandler
        The handler function to apply validation.
    info : ValidationInfo
        Information about the validation context.

    Returns
    -------
    Path
        The validated Path object.

    Raises
    ------
    AssertionError
        If the validation fails, i.e., if the path does not exist.

    Examples
    --------
    >> maybe_has_path('/some/path', handler, info)
    PosixPath('/some/path')
    """
    if not handler(v).exists():
        assert isinstance(v, Path), f'Cannot find a path for {v}'
    return handler(v)


ValidatedPath = Annotated[Path, WrapValidator(maybe_has_path)]


class ServiceLocator(BaseModel):
    """
    Pydantic model representing a service locator with validated paths.

    Attributes
    ----------
    dataloader : Dict[str, ValidatedPath]
        Dictionary mapping names to validated dataloader paths.
    experiments : ValidatedPath
        Path to the experiments file.
    neural_networks : Dict[str, ValidatedPath]
        Dictionary mapping names to validated neural network paths.
    physics_models : Dict[str, ValidatedPath]
        Dictionary mapping names to validated physics model paths.

    Examples
    --------
    >> locator = ServiceLocator(dataloader={"loader1": "/path/to/loader1"},
                                 experiments="/path/to/experiments",
                                 neural_networks={"nn1": "/path/to/nn1"},
                                 physics_models={"model1": "/path/to/model1"})
    """
    dataloader: Dict[str, ValidatedPath]
    experiments: ValidatedPath
    neural_networks: Dict[str, ValidatedPath]
    physics_models: Dict[str, ValidatedPath]
