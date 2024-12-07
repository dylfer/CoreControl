from flask import Blueprint, jsonify, request, send_file
import os
import time
import base64
from load import load

router = Blueprint('files', __name__, url_prefix='/files')

path_to_main = "./"
file_path_source = load()["file_path_source"]


class File:
    def __init__(self):
        pass

    def __check_file(file_name):
        print("check", os.path.join(path_to_main + file_path_source, file_name))
        if not os.path.isfile(os.path.join(path_to_main + file_path_source, file_name)):
            return jsonify({"error": "File not found"}), 404
        else:
            return False

    @classmethod
    def get_file(self, file_name):
        try:
            invalid = File.__check_file(file_name)
            if invalid:
                return invalid
            full_path = os.path.join(
                path_to_main + file_path_source, file_name)
            print("full", full_path)
            with open(full_path, 'rb') as f:
                content = f.read()
            try:
                content = content.decode('utf-8')
            except:
                content = base64.b64encode(content).decode("utf-8")
            print(content)
            size = os.path.getsize(full_path)
            creation_at = os.path.getctime(full_path)
            modified_at = os.path.getmtime(full_path)
            return jsonify(
                {"size": size, "created_at": creation_at,
                 "modified_at": modified_at, "data": content})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @classmethod
    def edit_file(self, file_name, content):
        try:
            invalid = File.__check_file(file_name)
            if invalid:
                return invalid
            with open(os.path.join(path_to_main + file_path_source, file_name), 'w') as f:
                f.write(content)
            return jsonify({"message": "File updated successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@router.route("/list")
def list_files():
    data = request.json
    path = data.get("path", "")
    try:
        items = os.listdir(path_to_main + file_path_source + path)
        files_info = []
        for item in items:
            item_path = os.path.join(
                path_to_main + file_path_source + path, item)
            if os.path.isdir(item_path):
                files_info.append({"name": item, "type": "directory"})
            else:
                files_info.append({"name": item, "type": "file"})
        return jsonify({"files": files_info})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@router.route("/get-file", methods=["POST"])
def get_file():
    file_name = request.json.get("file_name")
    print(file_name[0])
    if file_name[0] == "/" or file_name[0] == "\\":
        file_name = file_name[1:]
    return File.get_file(file_name)


@router.route("/edit-file", methods=["POST"])
def edit_file():
    file_name = request.json["file_name"]
    content = request.json["content"]
    return File.edit_file(file_name, content)
