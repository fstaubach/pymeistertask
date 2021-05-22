import requests

from .comments import CommentsAPI
from .labels import LabelsAPI
from .persons import PersonsAPI
from .projects import ProjectsAPI
from .sections import SectionsAPI
from .tasklabels import TaskLabelsAPI
from .tasks import TasksAPI
from .workintervals import WorkintervalsAPI
from .checklists import ChecklistsAPI
from .checklistitems import ChecklistItemsAPI
from .taskrelationships import TaskRelationshipsAPI


class MeisterTaskAPI(object):
    def __init__(self, bearer_token):
        self.session = requests.session()
        self.session.headers = {"Authorization": "Bearer {}".format(bearer_token)}

        # API endpoints
        self._comments = None
        self._labels = None
        self._persons = None
        self._projects = None
        self._sections = None
        self._tasklabels = None
        self._tasks = None
        self._workintervals = None
        self._checklists = None
        self._checklistitems = None
        self._taskrelationships = None

    @property
    def comments(self):
        if self._comments is None:
            self._comments = CommentsAPI(self)
        return self._comments

    @property
    def labels(self):
        if self._labels is None:
            self._labels = LabelsAPI(self)
        return self._labels

    @property
    def persons(self):
        if self._persons is None:
            self._persons = PersonsAPI(self)
        return self._persons

    @property
    def projects(self):
        if self._projects is None:
            self._projects = ProjectsAPI(self)
        return self._projects

    @property
    def sections(self):
        if self._sections is None:
            self._sections = SectionsAPI(self)
        return self._sections

    @property
    def tasklabels(self):
        if self._tasklabels is None:
            self._tasklabels = TaskLabelsAPI(self)
        return self._tasklabels

    @property
    def tasks(self):
        if self._tasks is None:
            self._tasks = TasksAPI(self)
        return self._tasks

    @property
    def workintervals(self):
        if self._workintervals is None:
            self._workintervals = WorkintervalsAPI(self)
        return self._workintervals

    @property
    def checklists(self):
        if self._checklists is None:
            self._checklists = ChecklistsAPI(self)
        return self._checklists

    @property
    def checklistitems(self):
        if self._checklistitems is None:
            self._checklistitems = ChecklistItemsAPI(self)
        return self._checklistitems

    @property
    def taskrelationships(self):
        if self._taskrelationships is None:
            self._taskrelationships = TaskRelationshipsAPI(self)
        return self._taskrelationships

    def __repr__(self):
        return "<MeisterTaskAPI>"
