class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into pairs and sort by position descending
        pairs = sorted(zip(position, speed), reverse=True)

        fleet = 0
        last_time = 0

        for pos, spe in pairs:
            # Calculate time to destination
            time = (target - pos) / spe

            # If this car's time is greater than the last fleet's time
            if time > last_time:
                fleet += 1
                last_time = time  # Update last_time for the new fleet

        return fleet