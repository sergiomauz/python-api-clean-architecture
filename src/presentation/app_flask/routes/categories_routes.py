
from dependency_injector.wiring import inject, Provide
from di_container_beta import DiContainerBeta
from application.use_cases.categories.commands.create_category import CreateCategoryDto
from presentation.app_flask.extended_flask import Blueprint, request
from presentation.app_flask.responses import ResponseOk


blueprint = Blueprint(
    "categories", 
    __name__, 
    url_prefix="/"
)

@blueprint.route("/categories", methods=["POST"])
@inject
async def create_category(
    use_case=Provide[DiContainerBeta.create_category_use_case]
):
    """ ToDo: DocString """
    request_json = request.get_json()
    dto = CreateCategoryDto(**request_json)
    vm = await use_case.execute(dto)

    return ResponseOk("'create_category', from extended Flask!", vm)

