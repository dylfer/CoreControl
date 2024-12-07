from flask import Blueprint, jsonify, request
import os

router = Blueprint('files', __name__, url_prefix='/files')

path_to_main = "./"


class File:
    def __init__(self):
        pass

    def __check_file(file_name):
        if file_name not in os.listdir(os.join(path_to_main, file_path_source)):
            return jsonify({"error": "File not found"}), 404
        else:
            return False

    @classmethod
    def get_file(file_name):
        try:
            invalid = File.__check_file(file_name)
            if invalid:
                return invalid
            with open(os.path.join(path_to_main, file_path_source, file_name), 'r') as f:
                content = f.read()
            return jsonify({"content": content})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @classmethod
    def edit_file(file_name, content):
        try:
            invalid = File.__check_file(file_name)
            if invalid:
                return invalid
            with open(os.path.join(path_to_main, file_path_source, file_name), 'w') as f:
                f.write(content)
            return jsonify({"message": "File updated successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@router.route("/list")
def list_files():
    data = request.json
    path = data.get("path")
    try:
        files = [f for f in os.listdir(os.path.join(
            path_to_main, file_path_source, path))]
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@router.route("/get-file", methods=["POST"])
def get_file():
    file_name = request.json["file_name"]
    return File.get_file(file_name)


@router.route("/edit-file", methods=["POST"])
def edit_file():
    file_name = request.json["file_name"]
    content = request.json["content"]
    return File.edit_file(file_name, content)
