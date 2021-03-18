# Async vs sync
1. Set `level=logging.DEBUG` at line 19 to see all log messages.
2. Pay attention, all coroutines work in the same process and thread
(you will see process in thread id if enable all log messages), therefore
data race condition is improssible here.

