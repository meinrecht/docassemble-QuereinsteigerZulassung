from docassemble.base.util import get_config
from zitadel_api import ZitadelAPI

def create_zitadel_user(first_name, last_name, email, password):
  config = get_config("zitadel")
  zitadel_api = ZitadelAPI(config["zitadel_url"], config["service_user_id"], config["service_key_id"])     
  user = zitadel_api.create_user(first_name, last_name, email, password)
  project_id = zitadel_api.find_project_by_name("Quereinsteiger")                                             
  zitadel_api.set_user_grant(project_id, user["userId"], ["quereinsteiger"])  