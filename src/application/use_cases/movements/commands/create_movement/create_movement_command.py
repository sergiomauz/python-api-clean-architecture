from http import HTTPStatus
from commons.enums import MovementType
from commons.utils import CustomParsers
from application.commons.validators import CustomValidator
from application.error_catalog import ErrorConstants
from application.exceptions.errors import CustomValidationError, CustomValidationErrorVm
from .create_movement_dto import CreateMovementDto


class CreateMovementCommand(CustomValidator):

    def __init__(self, dto:CreateMovementDto):
        self.partner_id = dto.partner_id
        self.product_id = dto.product_id
        self.movement_date = dto.movement_date
        self.quantity = dto.quantity
        self.movement_type = dto.movement_type

    def format_validation(self):
        errors = []
        if not self.partner_id or not isinstance(self.partner_id, int) or self.partner_id < 1:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_MOVEMENT_FORMAT00001.error_code,
                property_name=ErrorConstants.CREATE_MOVEMENT_FORMAT00001.property_name,                    
                error_message=ErrorConstants.CREATE_MOVEMENT_FORMAT00001.error_message
            ))    
        if not self.product_id or not isinstance(self.product_id, int) or self.product_id < 1:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_MOVEMENT_FORMAT00002.error_code,
                property_name=ErrorConstants.CREATE_MOVEMENT_FORMAT00002.property_name,                    
                error_message=ErrorConstants.CREATE_MOVEMENT_FORMAT00002.error_message
            ))    
        if not self.movement_date or not CustomParsers.are_valid_datetimes(self.movement_date):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_MOVEMENT_FORMAT00003.error_code,
                property_name=ErrorConstants.CREATE_MOVEMENT_FORMAT00003.property_name,                    
                error_message=ErrorConstants.CREATE_MOVEMENT_FORMAT00003.error_message
            ))  
        if not self.quantity or not isinstance(self.quantity, (int, float)) or self.quantity <= 0:
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_MOVEMENT_FORMAT00004.error_code,
                property_name=ErrorConstants.CREATE_MOVEMENT_FORMAT00004.property_name,                    
                error_message=ErrorConstants.CREATE_MOVEMENT_FORMAT00004.error_message
            ))
        if not (self.movement_type and MovementType.from_value(self.movement_type)):
            errors.append(CustomValidationErrorVm(
                error_code=ErrorConstants.CREATE_MOVEMENT_FORMAT00005.error_code,
                property_name=ErrorConstants.CREATE_MOVEMENT_FORMAT00005.property_name,                    
                error_message=ErrorConstants.CREATE_MOVEMENT_FORMAT00005.error_message.format(
                    movement_type=str(self.movement_type)
                )
            ))               
            
        if errors:
            raise CustomValidationError(
                None,
                errors,
                HTTPStatus.UNPROCESSABLE_ENTITY.value
            )

        return errors
