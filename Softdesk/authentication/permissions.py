from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée pour autoriser uniquement l'auteur d'une ressource à la modifier ou à la supprimer.
    Les autres utilisateurs ne peuvent que lire la ressource.
    """

    def has_object_permission(self, request, view, obj):
        # Autoriser les requêtes en lecture (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Vérifier si l'utilisateur est l'auteur de la ressource
        return obj.author == request.user

class IsContributorOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée pour autoriser uniquement les contributeurs d'un projet à accéder à ses ressources.
    Les autres utilisateurs ne peuvent que lire les ressources.
    """

    def has_object_permission(self, request, view, obj):
        # Autoriser les requêtes en lecture (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Vérifier si l'utilisateur est un contributeur du projet associé à la ressource
        return obj.project.contributors.filter(user=request.user).exists()
