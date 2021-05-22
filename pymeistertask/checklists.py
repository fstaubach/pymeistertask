from .resource import Resource, ResourceAPI


class Checklist(Resource):
    _repr_attrs = ("id", "task_id", "project_id", "name")

    def checklistitems(self):
        return self.api.checklistitems.filter_by_checklist(checklist_id=self.id)


class ChecklistsAPI(ResourceAPI):
    _resource = Checklist

    def create(self, project_id, data):
        return self._create_object(
            url="/projects/{project_id}/checklists".format(project_id=project_id), data=data
        )

    def create_in_task(self, task_id, data):
        return self._create_object(
            url="/tasks/{task_id}/checklists".format(task_id=task_id), data=data
        )

    def get(self, id):
        return self._get_object(url="/checklists/{id}".format(id=id))

    def update(self, id, data):
        return self._update_object(url="/checklists/{id}".format(id=id), data=data)

    def delete(self, id):
        return self._delete_object(url="/checklists/{id}".format(id=id))

    def filter_by_project(self, project_id, **kwargs):
        return self._get_list(url="/projects/{project_id}/checklists".format(project_id=project_id), **kwargs)

    def filter_by_task(self, task_id, **kwargs):
        return self._get_list(url="/tasks/{task_id}/checklists".format(task_id=task_id), **kwargs)
