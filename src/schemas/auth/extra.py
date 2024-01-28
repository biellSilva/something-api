from pydantic import RootModel, field_validator


class UserCpf(RootModel[str]):
    root: str

    @property
    def numbers(self):
        return "".join(filter(str.isdigit, self.root))

    @field_validator("root")
    @classmethod
    def formmating_cpf(cls, cpf: str | None) -> str | None:
        if not cpf:
            return None
        """
        This method is responsible for formatting the cpf.

        Example:
            input: "12345678909"
            output: "123.456.789-09"
        """
        cpf_numbers = "".join(filter(str.isdigit, cpf))
        return (
            f"{cpf_numbers[:3]}.{cpf_numbers[3:6]}.{cpf_numbers[6:9]}-{cpf_numbers[9:]}"
        )
