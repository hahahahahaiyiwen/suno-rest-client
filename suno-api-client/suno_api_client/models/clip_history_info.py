from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClipHistoryInfo")


@_attrs_define
class ClipHistoryInfo:
    """History info about the audio clip.

    Attributes:
        id (Union[Unset, str]): Clip id.
        continue_at (Union[Unset, float]): Continue at in seconds.
        type (Union[Unset, str]): Clip type.
        infill (Union[Unset, bool]): Infill or not.
    """

    id: Union[Unset, str] = UNSET
    continue_at: Union[Unset, float] = UNSET
    type: Union[Unset, str] = UNSET
    infill: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        continue_at = self.continue_at

        type = self.type

        infill = self.infill

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if continue_at is not UNSET:
            field_dict["continue_at"] = continue_at
        if type is not UNSET:
            field_dict["type"] = type
        if infill is not UNSET:
            field_dict["infill"] = infill

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        continue_at = d.pop("continue_at", UNSET)

        type = d.pop("type", UNSET)

        infill = d.pop("infill", UNSET)

        clip_history_info = cls(
            id=id,
            continue_at=continue_at,
            type=type,
            infill=infill,
        )

        clip_history_info.additional_properties = d
        return clip_history_info

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
