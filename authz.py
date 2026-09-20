"""Minimal object-level authorization logic for an API service."""

from dataclasses import dataclass
from enum import Enum


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


@dataclass(frozen=True)
class Principal:
    user_id: str
    role: Role


@dataclass(frozen=True)
class Resource:
    resource_id: str
    owner_id: str
    value: str


class ForbiddenError(PermissionError):
    pass


def can_read(principal: Principal, resource: Resource) -> bool:
    return principal.role == Role.ADMIN or principal.user_id == resource.owner_id


def can_update(principal: Principal, resource: Resource) -> bool:
    return principal.role == Role.ADMIN or principal.user_id == resource.owner_id


def require_read(principal: Principal, resource: Resource) -> Resource:
    if not can_read(principal, resource):
        raise ForbiddenError("principal is not authorized to read this resource")
    return resource


def update_value(
    principal: Principal, resource: Resource, new_value: str
) -> Resource:
    if not can_update(principal, resource):
        raise ForbiddenError("principal is not authorized to update this resource")
    return Resource(resource.resource_id, resource.owner_id, new_value)
