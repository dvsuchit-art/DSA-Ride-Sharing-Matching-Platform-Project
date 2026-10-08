from dataclasses import dataclass
@dataclass(frozen=True)
class Driver:
    id:str; x:float; y:float
@dataclass(frozen=True)
class Rider:
    id:str; x:float; y:float
@dataclass(frozen=True)
class Match:
    driver_index:int; rider_index:int; distance:float
