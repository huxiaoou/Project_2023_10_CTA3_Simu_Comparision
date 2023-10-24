from skyrim.falkreath import CLib1Tab1, CTable


def get_lib_struct_available_universe() -> CLib1Tab1:
    return CLib1Tab1(
        t_lib_name="available_universe.db",
        t_tab=CTable({
            "table_name": "available_universe",
            "primary_keys": {"trade_date": "TEXT", "instrument": "TEXT"},
            "value_columns": {"return": "REAL", "amount": "REAL"}
        })
    )


def get_lib_struct_signals(opt_id: str) -> CLib1Tab1:
    return CLib1Tab1(
        t_lib_name=f"{opt_id}.db",
        t_tab=CTable({
            "table_name": opt_id,
            "primary_keys": {"trade_date": "TEXT", "signal": "TEXT"},
            "value_columns": {"value": "REAL"},
        })
    )


database_structure: dict[str, CLib1Tab1] = {
    "available_universe": get_lib_struct_available_universe()
}
