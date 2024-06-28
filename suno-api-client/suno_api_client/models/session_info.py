from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionInfo")


@_attrs_define
class SessionInfo:
    """The info of the client session.

    Attributes:
        object_ (Union[Unset, str]):
        id (Union[Unset, str]):
        status (Union[Unset, str]):
        created_at (Union[Unset, float]):
        updated_at (Union[Unset, float]):
    """

    object_: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    created_at: Union[Unset, float] = UNSET
    updated_at: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_

        id = self.id

        status = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = d.pop("object", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        session_info = cls(
            object_=object_,
            id=id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        session_info.additional_properties = d
        return session_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
