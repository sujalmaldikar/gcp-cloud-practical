
class StoragePermissionError(Exception):
    pass


# Simulate the service account's Storage permission
storage_permission_granted = False


def access_storage():
    if not storage_permission_granted:
        raise StoragePermissionError(
            "403 Forbidden: Permission denied to access Cloud Storage."
        )

    print("SUCCESS: Cloud Storage access granted!")


print("TEST 1: Permission removed")

try:
    access_storage()
except StoragePermissionError as error:
    print(error)


print("\nTEST 2: Restoring permission")

storage_permission_granted = True

try:
    access_storage()
except StoragePermissionError as error:
    print(error)