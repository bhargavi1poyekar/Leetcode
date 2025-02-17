class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def backtrack(current, used):
            sequences.add(current)

            # Try adding each unused character to current sequence
            for pos, char in enumerate(tiles):
                if not used[pos]:
                    used[pos] = True
                    backtrack(current + char, used)
                    used[pos] = False


        sequences = set()
        used = [False] * len(tiles)

        # Generate all possible sequences including empty string
        backtrack("", used)

        # Subtract 1 to exclude empty string from count
        return len(sequences) - 1