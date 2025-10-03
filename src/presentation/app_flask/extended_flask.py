
from typing import List, Any, Callable
from flask import Flask, Blueprint, Response, jsonify, request, g


class ExtendedFlask(Flask):
    
    def include_blueprints(self, blueprints: List[Blueprint]):
        """ ToDo: DocString """
        for blueprint in blueprints:
            self.register_blueprint(blueprint)
