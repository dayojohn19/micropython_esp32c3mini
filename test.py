def brute_force_generator(target, charset=None, max_length=None):
    """
    Faster iterative brute-force in MicroPython.
    No recursion → better speed & no stack overflow.
    Prints every attempt.
    """
    if charset is None:
        # Keep charset small if possible — biggest speed factor!
        charset = "abcdefghijklmnopqrstuvwxyz0123456789!@#"

    charset_list = list(charset)          # faster access than string indexing
    n_chars = len(charset_list)

    if max_length is None:
        max_length = len(target) + 2

    print("Starting brute-force (iterative) for:", target)
    print("Charset size:", n_chars, "chars")
    print("Trying up to length:", max_length)

    import time
    start = time.time()

    for length in range(1, max_length + 1):
        print("\nTrying length", length, "... ({:,} combos)".format(n_chars ** length))

        # Current combination (as list of indices into charset)
        indices = [0] * length
        is_connected = False
        while not is_connected:
            # Build current string
            attempt = ''.join(charset_list[i] for i in indices)

                # every attempt
            # is_connected = connect_wifi(SSID,attempt)

            if attempt == target:
                end = time.time()
                diff = start - end
                print("\nFOUND after", diff, "ms")

                return attempt

            # Increment like an odometer (from right to left)
            pos = length - 1
            while pos >= 0:
                indices[pos] += 1
                if indices[pos] < n_chars:
                    break
                indices[pos] = 0
                pos -= 1

            if pos < 0:
                # All combinations for this length done
                break

    end = time.ticks_ms()
    print("\nNot found. Total time:", time.ticks_diff(end, start), "ms")
    return None

brute_force_generator('lea@0606')