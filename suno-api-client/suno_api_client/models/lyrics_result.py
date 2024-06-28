from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LyricsResult")


@_attrs_define
class LyricsResult:
    """The result of generated lyrics

    Attributes:
        text (Union[Unset, str]): Lyrics text.
        title (Union[Unset, str]): Lyrics title.
        status (Union[Unset, str]): The generated states include submitted, queued, streaming, complete.
    """

    text: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        title = self.title

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        status = d.pop("status", UNSET)

        lyrics_result = cls(
            text=text,
            title=title,
            status=status,
        )

        lyrics_result.additional_properties = d
        return lyrics_result

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
