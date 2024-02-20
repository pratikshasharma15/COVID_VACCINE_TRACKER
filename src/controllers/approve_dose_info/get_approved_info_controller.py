import logging
from flask import g

from utils.exceptions import CustomException
from handlers.approve_dose_handler import ApproveDoseHandler


logger = logging.getLogger(__name__)


class GetApprovedInfoController:
    '''
        Class that contains methods to get approved info.
    '''

    def __init__(self) -> None:
        self.approve_dose_handler = ApproveDoseHandler()


    def show_info_to_approve(self):
        """ 
            This method is used to show the data to be approved by admin. 
        """

        try:
            list = self.approve_dose_handler.get_list_to_approve()
            logger.info(f"[{g.request_id}] fetched the list of unapproved data")
            
            return {
                "unapproved data": list
            }, 200

        except CustomException as e:
            return e.dump(), e.code