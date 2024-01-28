"""
This module contains a class that performs CPF validations
"""

from typing import TYPE_CHECKING, Callable, Literal

from pydantic import field_validator

from src.domain.errors.auth import WrongCpfFormat


if TYPE_CHECKING:
    from src.schemas.auth.extra import UserCpf


class CpfValidator:
    root: str

    def __str__(self):
        return self.root

    def __repr__(self) -> str:
        return self.__str__()

    @field_validator("root", mode="before")
    @classmethod
    def check_valid_cpf(cls, cpf: str):
        """
        This classmethod is compatible
        with the pydantic.BaseModel input validator

        Example:
        ```python
        from pydantic import BaseModel
        from pydantic import ValidationError


        class User(BaseModel):
            ...
            cpf: CpfValidator

        user = User(..., cpf=CpfValidator(root="123.456.789-09")) # Ok
        try:
            user = User(..., cpf=CpfValidator(root="123.456.789-10")) # Error
        except ValidationError as err:
            print("error validating user")
        ```
        """

        if cls.is_valid_cpf(cpf):
            return cpf

    @classmethod
    def __get_validators(cls) -> list[Callable[[str], bool]]:
        """
        Return a list of validators needed to validate the cpf.
        """
        return [cls.check_length_cpf, cls.check_digit_validators]

    @classmethod
    def check_formatting_cpf(cls, cpf: str) -> bool:
        if len(cpf) == 14:
            points = [cpf[3], cpf[7]]
            trace = cpf[-3]
            if all(char == "." for char in points) and trace == "-":
                return True
        return False

    @classmethod
    def is_valid_cpf(cls, cpf: str) -> bool:
        return all(validator(cpf) for validator in cls.__get_validators())

    @classmethod
    def validate(cls, cpf: "str | UserCpf") -> str | None:
        cpf = cpf if isinstance(cpf, str) else cpf.root
        if cls.is_valid_cpf(cpf):
            return cpf
        raise WrongCpfFormat

    @classmethod
    def check_length_cpf(cls, cpf: str) -> bool:
        if len(cls.get_numbers_cpf(cpf)) == 11:
            return True
        return False

    @classmethod
    def check_digit_validators(cls, cpf: str) -> bool:
        if cls.check_first_validator_digit(cpf) and cls.check_second_validator_digit(
            cpf
        ):
            return True
        return False

    @classmethod
    def check_first_validator_digit(cls, cpf: str) -> str | None:
        return cls.__check_digit_verifyng(cpf, 9)

    @classmethod
    def check_second_validator_digit(cls, cpf: str) -> str | None:
        return cls.__check_digit_verifyng(cpf, 10)

    @classmethod
    def __check_digit_verifyng(
        cls, cpf: str, number_validator: Literal[9, 10]
    ) -> str | None:
        """
        This method checks the validator digits.
        """
        if number_validator not in [9, 10]:
            raise ValueError("Invalid number_validator: %s" % number_validator)

        cpf_numbers = cls.get_numbers_cpf(cpf)
        sum_of_products = sum(
            int(a) * b
            for a, b in zip(
                cpf_numbers[0:number_validator], range(number_validator + 1, 1, -1)
            )
        )
        expected_digit = (sum_of_products * 10 % 11) % 10
        digit_validator = int(cpf_numbers[number_validator])
        if digit_validator == expected_digit:
            return cpf

    @classmethod
    def get_numbers_cpf(cls, cpf: str) -> str:
        """
        This method return the numbers of cpf
        Examples:
            input: "123.456.789-10"
            output: "12345678910"
        """
        return "".join(filter(str.isdigit, cpf))
