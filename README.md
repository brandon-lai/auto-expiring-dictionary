# auto-expiring-dictionary
Data structure written in Python that handles auto-expiring keys.

Given a specific time to live, a key is no longer valid (inaccessible) once the duration has exceeded the time limit from the time of creation. All data associated with invalidated keys is automatically removed to reduce memory usage.
