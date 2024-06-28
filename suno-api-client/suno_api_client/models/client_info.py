from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_info import SessionInfo


T = TypeVar("T", bound="ClientInfo")


@_attrs_define
class ClientInfo:
    """The info of client.

    Attributes:
        object_ (Union[Unset, str]):
        id (Union[Unset, str]):
        sessions (Union[Unset, List['SessionInfo']]):
        last_active_session_id (Union[Unset, str]):
        created_at (Union[Unset, float]):
        updated_at (Union[Unset, float]):
    """

    object_: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    sessions: Union[Unset, List["SessionInfo"]] = UNSET
    last_active_session_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, float] = UNSET
    updated_at: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_

        id = self.id

        sessions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sessions, Unset):
            sessions = []
            for sessions_item_data in self.sessions:
                sessions_item = sessions_item_data.to_dict()
                sessions.append(sessions_item)

        last_active_session_id = self.last_active_session_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if last_active_session_id is not UNSET:
            field_dict["last_active_session_id"] = last_active_session_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.session_info import SessionInfo

        d = src_dict.copy()
        object_ = d.pop("object", UNSET)

        id = d.pop("id", UNSET)

        sessions = []
        _sessions = d.pop("sessions", UNSET)
        for sessions_item_data in _sessions or []:
            sessions_item = SessionInfo.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        last_active_session_id = d.pop("last_active_session_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        client_info = cls(
            object_=object_,
            id=id,
            sessions=sessions,
            last_active_session_id=last_active_session_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        client_info.additional_properties = d
        return client_info

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
