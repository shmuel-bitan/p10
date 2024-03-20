from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Project, Issue, Comment, Contributor
from .serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    IssueListSerializer,
    IssueDetailSerializer,
    CommentListSerializer,
    CommentDetailSerializer,
    ContributorSerializer,
)
from .permissions import (
    IsAuthor,
    IsContributor,
    IsContributorForContributor,
    isAuthorForContributor,
    IsContributorForIssue,
    IsAuthorOfIssue,
    IsContributorForComment,
    IsAuthorOfComment,
)


class ProjectViewSet(ModelViewSet):
    """A class representation of a project.

    Arguments:
        ModelViewSet -- class ModelViewSet

    Returns:
        None
    """

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self) -> object:
        """Method to get all the project of the database.

        Returns:
            object: queryset containing all projects
        """
        return Project.objects.all()

    def get_serializer_class(self):
        if not self.action == "list":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_permissions(self) -> list:
        """Method to give permission to user

        Returns:
            list
        """
        if self.action in ["create"]:
            permission_classes = [IsAuthenticated]
        elif self.action in ["list", "retrieve"]:
            permission_classes = [
                IsAuthenticated,
                IsContributor | IsAuthor,
            ]
        else:
            permission_classes = [IsAuthor]
        return [permission() for permission in permission_classes]


class ContributorViewSet(ModelViewSet):
    """A class representation of a contributor.

    Arguments:
        ModelViewSet -- class ModelViewSet

    Returns:
        None
    """

    serializer_class = ContributorSerializer

    def get_queryset(self) -> object:
        """Method to get all the project's contributors.

        Returns:
            object: queryset containing all contributors
        """
        contributors = Contributor.objects.filter(
            project=self.kwargs["project_pk"]
            )
        return contributors

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions_classes = [IsContributorForContributor]
        else:
            permissions_classes = [isAuthorForContributor]

        return [permission() for permission in permissions_classes]


class IssueViewSet(ModelViewSet):
    """A class representation of a issue.

    Arguments:
        ModelViewSet -- class ModelViewSet

    Returns:
        None
    """

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_permissions(self) -> list:
        """Method to give permission to user

        Returns:
            list
        """
        if self.action in ["list", "retrieve", "create"]:
            permission_classes = [
                IsAuthenticated & IsContributorForIssue
            ]
        else:
            permission_classes = [IsAuthorOfIssue]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
            if not self.action == "list":
                return self.detail_serializer_class
            return super().get_serializer_class()

    def get_queryset(self) -> object:
        """Method to get all the project's issues.

        Returns:
            object: queryset containing all issues
        """
        issues = Issue.objects.filter(project=self.kwargs["project_pk"])
        return issues


class CommentViewSet(ModelViewSet):
    """A class representation of a comment.

    Arguments:
        ModelViewSet -- class ModelViewSet

    Returns:
        None
    """

    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer

    def get_queryset(self) -> object:
        """Method to get all the issue's comments.

        Returns:
            object: queryset containing all comments
        """
        comments = Comment.objects.filter(issue=self.kwargs["issue_pk"])
        return comments
