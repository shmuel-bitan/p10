from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from .models import Project, Contributor


class IsAuthor(permissions.BasePermission):
    """A class that reprensents a permission to check if the current
    user is the author of the project.

    Arguments:
        permissions -- a class BasePermission
    """

    def has_object_permission(
            self,
            request: str,
            view: object,
            obj: object
    ) -> bool:
        """Method to check if the current
        user is the author of the project.

        Arguments:
            request -- str: a request
            view -- obj: a view
            obj -- obj: an object

        Returns:
            bool
        """
        return obj.author == request.user


class IsContributorForContributor(permissions.BasePermission):
    """A class thats represents autorization to the contributor of a project
    for the contributors ressource.

    Arguments:
        permissions -- a BasePermission class
    """

    def has_permission(self, request: str, view: str):
        """Method to check if the user is the author of the project
        for post method and contributor for other methods.

        Arguments:
            request -- str: a request
            view -- str: a view

        Returns:
            bool
        """
        try:
            project = Project.objects.get(id=view.kwargs["project_pk"])
        except ObjectDoesNotExist:
            return False
        if project:
            contributors = Contributor.objects.filter(project=project)
            if request.method in permissions.SAFE_METHODS \
                    and request.user.is_authenticated \
                    and contributors.filter(user=request.user):
                return True
            elif request.method == 'POST' \
                    and request.user.is_authenticated \
                    and project.author == request.user:
                return True
            else:
                return False
        return False


class isAuthorForContributor(permissions.BasePermission):
    """A class thats represents autorization to the author of a project
    for the contributors ressource.

    Arguments:
        permissions -- a BasePermission class
    """

    def has_permission(self, request: str, view: str):
        """Method to check if the user is the author of the project
        for post, update or delete a contributor.

        Arguments:
            request -- str: a request
            view -- str: a view

        Returns:
            bool
        """
        try:
            project = Project.objects.get(id=view.kwargs["project_pk"])
        except ObjectDoesNotExist:
            return False
        if project:
            if request.method in ['POST', 'DELETE', 'UPDATE'] \
                    and request.user.is_authenticated \
                    and project.author == request.user:
                return True
        return False


class IsContributor(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is a project's contributor.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is a project's contributor.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        contributors = Contributor.objects.filter(project=obj)
        return contributors.filter(user=request.user)


class IsContributorForIssue(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is a project's contributor.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_permission(self, request: str, view: object):
        """A method to check if current user
        is a project's contributor.

        Arguments:
            request -- str: a request
            view -- obj: a view

        Returns:
            bool
        """

        try:
            project = Project.objects.get(id=view.kwargs["project_pk"])
        except ObjectDoesNotExist:
            return False
        return project.contributors.filter(user=request.user)


class IsAuthorOfIssue(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is the author of the issue.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is the author of the issue.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        return obj.author == request.user


class IsContributorForComment(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is a project's contributor.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_permission(self, request: str, view: object):
        """A method to check if current user
        is a project's contributor.

        Arguments:
            request -- str: a request
            view -- obj: a view

        Returns:
            bool
        """

        try:
            project = Project.objects.get(id=view.kwargs["project_pk"])
        except ObjectDoesNotExist:
            return False
        contributors = Contributor.objects.filter(project=project)
        return contributors.filter(user=request.user)

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is a project's contributor.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        try:
            project = Project.objects.get(id=view.kwargs["project_pk"])
        except ObjectDoesNotExist:
            return False
        contributors = Contributor.objects.filter(project=project)
        return contributors.filter(user=request.user)


class IsAuthorOfComment(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is the author of the comment.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is the author of the comment.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        return obj.author == request.user