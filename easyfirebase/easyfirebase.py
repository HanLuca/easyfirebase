import firebase_admin
from firebase_admin import credentials, db, storage

"""
2024.08.21 New Project
Easy use Firebase Module
"""

class EasyFirebase:
    def __init__(self, database_url, credentials_file):
        """
        Initialize a connection to the Firebase database.

        Parameters:
        database_url -- The URL of the Firebase Realtime Database (str)
        credentials_file -- Path to the Firebase service account .json file (str)
        """
        self.database_url = database_url
        self.credentials_file = credentials_file
        self._initialize_firebase()

    def _initialize_firebase(self):
        """
        Internal method to initialize the Firebase app with the provided credentials.
        """
        if not firebase_admin._apps:
            cred = credentials.Certificate(self.credentials_file)
            firebase_admin.initialize_app(cred, {
                'databaseURL': self.database_url
            })

    def save_data(self, path, data):
        """
        Save data to the specified path in the Firebase Realtime Database.

        Parameters:
        path -- The path in the database where the data should be saved (str)
        data -- The data to save, which can be a dictionary or list (dict or list)
        """
        ref = db.reference(path)
        ref.set(data)

    def load_data(self, path):
        """
        Load data from the specified path in the Firebase Realtime Database.

        Parameters:
        
        path -- The path in the database to load the data from (str)

        Returns:
        The data retrieved from the database, or None if no data is found.
        """
        ref = db.reference(path)
        return ref.get()

    def update_data(self, path, data):
        """
        Update data at the specified path in the Firebase Realtime Database.

        Parameters:
        path -- The path in the database where the data should be updated (str)
        data -- The data to update, which can be a dictionary or list (dict or list)
        """
        ref = db.reference(path)
        ref.update(data)

    def delete_data(self, path):
        """
        Delete data at the specified path in the Firebase Realtime Database.

        Parameters:
        path -- The path in the database where the data should be deleted (str)
        """
        ref = db.reference(path)
        ref.delete()

    def upload_file(self, file_path, storage_bucket, destination_path):
        """
        Upload a file to Firebase Cloud Storage.

        Parameters:
        file_path -- Local path to the file to be uploaded (str)
        storage_bucket -- The name of the Firebase storage bucket (str)
        destination_path -- The path in the storage bucket where the file will be stored (str)
        """
        bucket = storage.bucket(storage_bucket)
        blob = bucket.blob(destination_path)
        blob.upload_from_filename(file_path)

    def download_file(self, storage_bucket, source_path, destination_path):
        """
        Download a file from Firebase Cloud Storage.

        Parameters:
        storage_bucket -- The name of the Firebase storage bucket (str)
        source_path -- The path in the storage bucket where the file is stored (str)
        destination_path -- Local path where the file will be saved (str)
        """
        bucket = storage.bucket(storage_bucket)
        blob = bucket.blob(source_path)
        blob.download_to_filename(destination_path)
