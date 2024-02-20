import logging
from flask import g
from flask_jwt_extended import get_jwt_identity

from utils.exceptions import CustomException
from handlers.dose_handlers import DoseHandlers


logger = logging.getLogger(__name__)


class UpdateDoseController:
    '''
        This class contains methods to update dose details.
    '''
    
    def __init__(self) -> None:
        self.dose_handler = DoseHandlers()


    def update_dose_info(self, update_dose_info) -> None:
        """ This method is used to update the dose 2 details by an employee if already vaccinated with dose 1. """

        try:
            user_id = get_jwt_identity()
            self.dose_handler.update_dose_info(
                user_id,
                update_dose_info["vaccine_name"],
                update_dose_info["dose_date"],
                update_dose_info["dose_cid"]
            )
            logger.infp(f"[{g.request_id}] updated dose details")

            return {
                "message": "Dose details updated successfully!"
            }
        except CustomException as e:
            return e.dump(), e.code
