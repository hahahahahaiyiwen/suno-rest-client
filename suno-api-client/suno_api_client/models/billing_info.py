from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingInfo")


@_attrs_define
class BillingInfo:
    """The info of billing.

    Attributes:
        total_credits_left (Union[Unset, float]): Remaining credits.
        period (Union[Unset, str]): Period
        monthly_limit (Union[Unset, float]): Monthly limit
        monthly_usage (Union[Unset, float]): Monthly usage
    """

    total_credits_left: Union[Unset, float] = UNSET
    period: Union[Unset, str] = UNSET
    monthly_limit: Union[Unset, float] = UNSET
    monthly_usage: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_credits_left = self.total_credits_left

        period = self.period

        monthly_limit = self.monthly_limit

        monthly_usage = self.monthly_usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_credits_left is not UNSET:
            field_dict["total_credits_left"] = total_credits_left
        if period is not UNSET:
            field_dict["period"] = period
        if monthly_limit is not UNSET:
            field_dict["monthly_limit"] = monthly_limit
        if monthly_usage is not UNSET:
            field_dict["monthly_usage"] = monthly_usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_credits_left = d.pop("total_credits_left", UNSET)

        period = d.pop("period", UNSET)

        monthly_limit = d.pop("monthly_limit", UNSET)

        monthly_usage = d.pop("monthly_usage", UNSET)

        billing_info = cls(
            total_credits_left=total_credits_left,
            period=period,
            monthly_limit=monthly_limit,
            monthly_usage=monthly_usage,
        )

        billing_info.additional_properties = d
        return billing_info

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
