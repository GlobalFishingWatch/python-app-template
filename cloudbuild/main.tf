module "trigger_push_to_tag" {
  source              = "git::https://github.com/GlobalFishingWatch/gfw-terraform-modules.git//modules/cloudbuild-trigger?ref=v0.6.7"
  registry_artifact   = "core"
  repo_name           = "python-app-template"
  tag                 = ".*"
  trigger_description = "Builds and publishes a Docker image on every tag push."
}

module "trigger_push_to_main" {
  source              = "git::https://github.com/GlobalFishingWatch/gfw-terraform-modules.git//modules/cloudbuild-trigger?ref=v0.6.7"
  registry_artifact   = "core"
  repo_name           = "python-app-template"
  branch              = "main"
  trigger_description = "Builds and publishes a Docker image on every push to the main branch."
}
