class Solution:

    def encode(self, strs: List[str]) -> str:
        return '..||..'.join([str(len(strs))]+strs)
    def decode(self, s: str) -> List[str]:
        s = s.split('..||..')
        return s[1:]