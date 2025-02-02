"""
globalwarmingpotentials
-----------------------

"""

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions


def as_frame():
    """Return Global Warming Potentials as a Pandas DataFrame."""
    try:
        import pandas as pd
    except ImportError:
        raise ImportError(
            "pandas is required for reading global warming "
            "potentials as a Data Frame."
        ) from None

    import importlib.resources as pkg_resources

    return pd.read_csv(
        pkg_resources.open_text(
            "globalwarmingpotentials", "globalwarmingpotentials.csv"
        ),
        index_col=0,
        comment="#",
    )


data = {
    "SARGWP100": {
        "CH4": 21.0,
        "N2O": 310.0,
        "CFC11": 3800.0,
        "CFC12": 8100.0,
        "CFC113": 4800.0,
        "Halon1301": 5400.0,
        "CCl4": 1400.0,
        "CH3CCl3": 100.0,
        "HCFC22": 1500.0,
        "HCFC123": 90.0,
        "HCFC124": 470.0,
        "HCFC141b": 600.0,
        "HCFC142b": 1800.0,
        "HFC23": 11700.0,
        "HFC32": 650.0,
        "HFC41": 150.0,
        "HFC125": 2800.0,
        "HFC134": 1000.0,
        "HFC134a": 1300.0,
        "HFC143": 300.0,
        "HFC143a": 3800.0,
        "HFC152a": 140.0,
        "HFC227ea": 2900.0,
        "HFC236fa": 6300.0,
        "HFC245ca": 560.0,
        "HFC4310mee": 1300.0,
        "SF6": 23900.0,
        "CF4": 6500.0,
        "C2F6": 9200.0,
        "C3F8": 7000.0,
        "cC4F8": 8700.0,
        "C4F10": 7000.0,
        "C5F12": 7500.0,
        "C6F14": 7400.0,
        "CHCl3": 4.0,
        "CH2Cl2": 9.0,
    },
    "AR4GWP100": {
        "CH4": 25.0,
        "N2O": 298.0,
        "CFC11": 4750.0,
        "CFC12": 10900.0,
        "CFC13": 14400.0,
        "CFC113": 6130.0,
        "CFC114": 10000.0,
        "CFC115": 7370.0,
        "Halon1301": 7140.0,
        "Halon1211": 1890.0,
        "Halon2402": 1640.0,
        "CCl4": 1400.0,
        "CH3Br": 5.0,
        "CH3CCl3": 146.0,
        "HCFC22": 1810.0,
        "HCFC123": 77.0,
        "HCFC124": 609.0,
        "HCFC141b": 725.0,
        "HCFC142b": 2310.0,
        "HCFC225ca": 122.0,
        "HCFC225cb": 595.0,
        "HFC23": 14800.0,
        "HFC32": 675.0,
        "HFC125": 3500.0,
        "HFC134a": 1430.0,
        "HFC143a": 4470.0,
        "HFC152a": 124.0,
        "HFC227ea": 3220.0,
        "HFC236fa": 9810.0,
        "HFC245fa": 1030.0,
        "HFC365mfc": 794.0,
        "HFC4310mee": 1640.0,
        "SF6": 22800.0,
        "NF3": 17200.0,
        "CF4": 7390.0,
        "C2F6": 12200.0,
        "C3F8": 8830.0,
        "cC4F8": 10300.0,
        "C4F10": 8860.0,
        "C5F12": 9160.0,
        "C6F14": 9300.0,
        "SF5CF3": 17700.0,
        "HFE125": 14900.0,
        "HFE134": 6320.0,
        "HFE143a": 756.0,
        "HCFE235da2": 350.0,
        "HFE245cb2": 708.0,
        "HFE245fa2": 659.0,
        "HFE347mcc3": 575.0,
        "HFE347pcf2": 580.0,
        "HFE356pcc3": 110.0,
        "HFE449sl": 297.0,
        "HFE569sf2": 59.0,
        "HFE4310pccc124": 1870.0,
        "HFE236ca12": 2800.0,
        "HFE338pcc13": 1500.0,
        "PFPMIE": 10300.0,
        "CH2Cl2": 8.7,
        "CH3Cl": 13.0,
    },
    "AR5GWP100": {
        "CH4": 28.0,
        "N2O": 265.0,
        "CFC11": 4660.0,
        "CFC12": 10200.0,
        "CFC13": 13900.0,
        "CFC113": 5820.0,
        "CFC114": 8590.0,
        "CFC115": 7670.0,
        "Halon1301": 6290.0,
        "Halon1211": 1750.0,
        "Halon2402": 1470.0,
        "CCl4": 1730.0,
        "CH3Br": 2.0,
        "CH3CCl3": 160.0,
        "HCFC21": 148.0,
        "HCFC22": 1760.0,
        "HCFC123": 79.0,
        "HCFC124": 527.0,
        "HCFC141b": 782.0,
        "HCFC142b": 1980.0,
        "HCFC225ca": 127.0,
        "HCFC225cb": 525.0,
        "HFC23": 12400.0,
        "HFC32": 677.0,
        "HFC41": 116.0,
        "HFC125": 3170.0,
        "HFC134": 1120.0,
        "HFC134a": 1300.0,
        "HFC143": 328.0,
        "HFC143a": 4800.0,
        "HFC152": 16.0,
        "HFC152a": 138.0,
        "HFC161": 4.0,
        "HFC227ea": 3350.0,
        "HFC236cb": 1210.0,
        "HFC236ea": 1330.0,
        "HFC236fa": 8060.0,
        "HFC245ca": 716.0,
        "HFC245fa": 858.0,
        "HFC365mfc": 804.0,
        "HFC4310mee": 1650.0,
        "SO2F2": 4090.0,
        "SF6": 23500.0,
        "NF3": 16100.0,
        "CF4": 6630.0,
        "C2F6": 11100.0,
        "C3F8": 8900.0,
        "cC4F8": 9540.0,
        "C4F10": 9200.0,
        "C5F12": 8550.0,
        "C6F14": 7910.0,
        "C7F16": 7820.0,
        "C8F18": 7620.0,
        "C10F18": 7190.0,
        "SF5CF3": 17400.0,
        "cC3F6": 9200.0,
        "HFE125": 12400.0,
        "HFE134": 5560.0,
        "HFE143a": 523.0,
        "HCFE235da2": 491.0,
        "HFE245cb2": 654.0,
        "HFE245fa2": 812.0,
        "HFE347mcc3": 530.0,
        "HFE347pcf2": 889.0,
        "HFE356pcc3": 413.0,
        "HFE449sl": 421.0,
        "HFE569sf2": 57.0,
        "HFE4310pccc124": 2820.0,
        "HFE236ca12": 5350.0,
        "HFE338pcc13": 2910.0,
        "HFE227ea": 6450.0,
        "HFE236ea2": 1790.0,
        "HFE236fa": 979.0,
        "HFE245fa1": 828.0,
        "HFE263fb2": 1.0,
        "HFE329mcc2": 3070.0,
        "HFE338mcf2": 929.0,
        "HFE347mcf2": 854.0,
        "HFE356mec3": 387.0,
        "HFE356pcf2": 719.0,
        "HFE356pcf3": 446.0,
        "HFE365mcf3": 1.0,
        "HFE374pc2": 627.0,
        "PFPMIE": 9710.0,
        "CHCl3": 16.0,
        "CH2Cl2": 9.0,
        "CH3Cl": 12.0,
        "Halon1201": 376.0,
    },
    "AR5CCFGWP100": {
        "CH4": 34,
        "N2O": 298,
        "CFC11": 5352,
        "CFC12": 11547,
        "CFC13": 15451,
        "CFC113": 6586,
        "CFC114": 9615,
        "CFC115": 8516,
        "Halon1301": 7154,
        "Halon1211": 2070,
        "Halon2402": 1734,
        "Halon1202": 280,
        "CCl4": 2019,
        "CH3Br": 3,
        "CH3CCl3": 193,
        "HCFC21": 179,
        "HCFC22": 2106,
        "HCFC123": 96,
        "HCFC124": 635,
        "HCFC141b": 938,
        "HCFC142b": 2345,
        "HCFC225ca": 155,
        "HCFC225cb": 633,
        "HFC23": 13856,
        "HFC32": 817,
        "HFC41": 141,
        "HFC125": 3691,
        "HFC134": 1337,
        "HFC134a": 1549,
        "HFC143": 397,
        "HFC143a": 5508,
        "HFC152": 20,
        "HFC152a": 167,
        "HFC161": 4,
        "HFC227ea": 3860,
        "HFC236cb": 1438,
        "HFC236ea": 1596,
        "HFC236fa": 8998,
        "HFC245ca": 863,
        "HFC245fa": 1032,
        "HFC365mfc": 966,
        "HFC4310mee": 1952,
        "SO2F2": 4732,
        "SF6": 26087,
        "NF3": 17885,
        "CF4": 7349,
        "C2F6": 12340,
        "C3F8": 9878,
        "cC4F8": 10592,
        "C4F10": 10213,
        "C5F12": 9484,
        "C6F14": 8780,
        "C7F16": 8681,
        "C8F18": 8456,
        "C10F18": 7977,
        "SF5CF3": 19396,
        "cC3F6": 10208,
        "HFE125": 13951,
        "HFE134": 6512,
        "HFE143a": 632,
        "HCFE235da2": 595,
        "HFE245cb2": 790,
        "HFE245fa2": 981,
        "HFE347mcc3": 641,
        "HFE347pcf2": 1072,
        "HFE356pcc3": 500,
        "HFE449sl": 509,
        "HFE569sf2": 69,
        "HFE4310pccc124": 3353,
        "HFE236ca12": 6260,
        "HFE338pcc13": 3466,
        "HFE227ea": 7377,
        "HFE236ea2": 2143,
        "HFE236fa": 1177,
        "HFE245fa1": 997,
        "HFE263fb2": 2,
        "HFE329mcc2": 3598,
        "HFE338mcf2": 1118,
        "HFE347mcf2": 1028,
        "HFE356mec3": 468,
        "HFE356pcf2": 867,
        "HFE356pcf3": 540,
        "HFE365mcf3": 1,
        "HFE374pc2": 758,
        "PFPMIE": 10789,
        "CHCl3": 20,
        "CH2Cl2": 11,
        "CH3Cl": 15,
        "Halon1201": 454,
    },
}
