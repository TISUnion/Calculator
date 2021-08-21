from typing import List

from mcdreforged.api.utils import Serializable


class Configure(Serializable):
	max_result_length = 1000  # maximum result string length
	max_power_length = 10000  # simpleeval.MAX_POWER override
	enable_simpleeval = True  # if enable simpleeval for better calculator if it's doable
	function_blacklist: List[str] = [
		'exp', 'expm1', 'ldexp', 'pow', 'factorial'
	]
