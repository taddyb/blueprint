import logging

from omegaconf import DictConfig
from pydantic import ValidationError

from blueprint._config_models import ServiceLocator

log = logging.getLogger(__name__)


def validate(cfg: DictConfig) -> 'ServiceLocator':
    """
    Validate the provided configuration against the ServiceLocator model.

    Parameters
    ----------
    cfg : DictConfig
        The OmegaConf configuration object to be validated.

    Returns
    -------
    ServiceLocator
        The validated ServiceLocator object, if validation is successful.

    Raises
    ------
    ValidationError
        If the provided configuration does not conform to the ServiceLocator model.

    Examples
    --------
    >> cfg = OmegaConf.create({"services": {"dataloader": ...}})
    >> validated_locator = validate(cfg)
    """
    try:
        validated_locator = ServiceLocator.model_validate(cfg.services)
    except ValidationError as e:
        raise e
    return validated_locator
