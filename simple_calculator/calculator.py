import ast
import math
import operator
from abc import ABC
from typing import Optional, Union

import simpleeval

from simple_calculator.configure import Configure

RESULT = Union[int, float, str, bool]


class Calculator(ABC):
	def __init__(self, config: Optional[Configure]):
		self.config = config

	def calculate(self, expression: str) -> Optional[RESULT]:
		"""
		Return int or float or str or bool for the result
		Return None for ignoring input
		Raise whatever if necessary
		"""
		try:
			return self._calculate(expression)
		except Exception as e:
			return '{}: {}'.format(type(e).__name__, e)

	def _calculate(self, expression: str) -> Optional[RESULT]:
		raise NotImplementedError()


class NaiveCalculator(Calculator):
	def _calculate(self, expression: str) -> Optional[RESULT]:
		whitelist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', '+', '-', '*', '/', '(', ')', '<', '>', '=']
		expression = expression.replace('**', '')  # to avoid eeasee, no power operator
		text_clean = ''
		for c in expression:
			if c in whitelist:
				text_clean += c

		if len(text_clean) == 0:
			return None
		return eval(text_clean)


class SimpleevalCalculator(Calculator):
	def _calculate(self, expression: str) -> Optional[RESULT]:
		def merge(a: dict, b: dict):
			ret = a.copy()
			ret.update(b)
			return ret

		simpleeval.MAX_POWER = self.config.max_power_length
		s = simpleeval.SimpleEval(
			operators=merge(simpleeval.DEFAULT_OPERATORS, {
				ast.BitXor: operator.xor,
				ast.BitAnd: operator.and_,
				ast.BitOr: operator.or_,
				ast.RShift: operator.rshift,
				ast.LShift: operator.lshift,
			})
		)
		for k, v in math.__dict__.items():
			if not k.startswith('_'):
				if type(v) in [int, float]:
					s.names[k] = v
				elif callable(v) and k not in ['exp', 'expm1', 'ldexp', 'pow', 'factorial']:
					s.functions[k] = v
		s.functions.update({
			'hex': lambda x: hex(x).replace('0x', '', 1).rstrip('L').upper(),
			'bin': lambda x: bin(x).replace('0b', '', 1).rstrip('L'),
			'oct': lambda x: oct(x).replace('0o', '', 1).rstrip('L'),
			'bool': bool
		})
		return s.eval(expression)
