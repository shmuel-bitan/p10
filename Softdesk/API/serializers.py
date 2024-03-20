from rest_framework import serializers

from .models import Project, Issue, Comment, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    """A class representation of a contributor serializer.

    Arguments:
        serializers -- class ModelSerializer
    """

    class Meta:
        model = Contributor
        fields = ["id", "created_time", "user", "project"]
        read_only_fields = ["id", "author", "project"]

    def create(self, validated_data):
        project = Project.objects.get(
            id=self.context["view"].kwargs["project_pk"]
        )
        contributor = Contributor.objects.create(
            user=validated_data["user"],
            project=project)
        contributor.save()

        return contributor


class ProjectListSerializer(serializers.ModelSerializer):
    """A class representation of a contributor serializer.

    Arguments:
        serializers -- class ModelSerializer
    Returns:
        None
    """

    class Meta:
        model = Project
        fields = ["id", "author", "title", "description", "project_type"]
        read_only_fields = ["id", "author"]
        extra_kwargs = {
            "description": {"write_only": True},
            "project_type": {"write_only": True},
        }

    def create(self, validated_data: list) -> object:
        """Method to create a project instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a project object
        """
        request = self.context.get("request", None)
        if request:
            user = request.user
        project = Project(
            title=validated_data["title"],
            description=validated_data["description"],
            project_type=validated_data["project_type"],
            author=user,
        )

        project.save()
        contributor = Contributor(user=project.author, project=project)
        contributor.save()

        return project


class ProjectDetailSerializer(serializers.ModelSerializer):
    """A class representation of a contributor serializer.

    Arguments:
        serializers -- class ModelSerializer
    Returns:
        None
    """

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["id", "author"]

    contributors = ContributorSerializer(many=True, read_only=True)

    def create(self, validated_data: list) -> object:
        """Method to create a project instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a project object
        """
        request = self.context.get("request", None)
        if request:
            user = request.user
        project = Project(
            title=validated_data["title"],
            description=validated_data["description"],
            project_type=validated_data["project_type"],
            author=user,
        )

        project.save()
        contributor = Contributor(user=project.author, project=project)
        contributor.save()

        return project


class IssueListSerializer(serializers.ModelSerializer):
    """A class representation of a issue list serializer.

    Arguments:
        serializers -- class ModelSerializer
    """

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ["author", "id"]
        extra_kwargs = {
            "title": {"write_only": True},
            "description": {"write_only": True},
            "project": {"write_only": True},
            "priority": {"write_only": True},
            "tag": {"write_only": True},
            "status": {"write_only": True},
        }

    def create(self, validated_data: list) -> object:
        """Method to create a issue instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a issue object
        """
        project = Project.objects.get(
            id=self.context["view"].kwargs["project_pk"]
        )
        request = self.context.get("request", None)
        if request:
            user = request.user

        # vérification de l'assignation à un contributeur
        if "assign_to" in validated_data:
            contributor = validated_data['assign_to']
            if contributor.project != project:
                raise serializers.ValidationError("Le contributeur n'appartient pas au projet.")

        issue = Issue.objects.create(
            assign_to=contributor,
            project=project,
            title=validated_data["title"],
            description=validated_data["description"],
            tag=validated_data["tag"],
            priority=validated_data["priority"],
            status=validated_data["status"],
            author=user,
        )

        return issue


class IssueDetailSerializer(serializers.ModelSerializer):
    """A class representation of a issue detail serializer.

    Arguments:
        serializers -- class ModelSerializer
    """

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ["author", "id"]

    def create(self, validated_data: list) -> object:
        """Method to create a issue instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a issue object
        """
        project = Project.objects.get(
            id=self.context["view"].kwargs["project_pk"]
        )
        request = self.context.get("request", None)
        if request:
            user = request.user

        # vérification de l'assignation à un contributeur
        if "assign_to" in validated_data:
            contributor = validated_data['assign_to']
            if contributor.project != project:
                raise serializers.ValidationError("Le contributeur n'appartient pas au projet.")

        issue = Issue.objects.create(
            assign_to=contributor,
            project=project,
            title=validated_data["title"],
            description=validated_data["description"],
            tag=validated_data["tag"],
            priority=validated_data["priority"],
            status=validated_data["status"],
            author=user,
        )

        return issue


class CommentListSerializer(serializers.ModelSerializer):
    """A class representation of a comment serializer.

    Arguments:
        serializers -- class ModelSerializer
    """

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['id', "author", "uuid"]
        extra_kwargs = {
            "text": {"write_only": True},
            "issue": {"write_only": True},
        }

    def create(self, validated_data: list) -> object:
        """Method to create a comment instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a comment object
        """
        issue = Issue.objects.get(id=self.context["view"].kwargs["issue_pk"])
        request = self.context.get("request", None)
        if request:
            user = request.user
        comment = Comment.objects.create(
            text=validated_data["text"], issue=issue, author=user
        )

        return comment


class CommentDetailSerializer(serializers.ModelSerializer):
    """A class representation of a comment serializer.

    Arguments:
        serializers -- class ModelSerializer
    """

    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data: list) -> object:
        """Method to create a comment instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a comment object
        """
        issue = Issue.objects.get(id=self.context["view"].kwargs["issue_pk"])
        request = self.context.get("request", None)
        if request:
            user = request.user
        comment = Comment.objects.create(
            text=validated_data["text"], issue=issue, author=user
        )

        return comment