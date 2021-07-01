"""A video player class."""
from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    prev_played=''
    paused=''
    playlist_list=[]
    Video_in_playlist_list=[]
    '''[[v1 in p1, v2 in p1 ....],[v1 in p2,...],[],[],[],...]'''
    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        all_video_list=[]
        for i in range(len(all_videos)):
            tags=all_videos[i].tags
            video_id=all_videos[i].video_id
            title=all_videos[i].title
            all_video_list.append(f" {title} ({video_id}) [{' '.join(tags)}]")
            all_video_list.sort()
        print("\n".join(all_video_list))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        all_videos = self._video_library.get_all_videos()
        title_list=[]
        video_id_list=[]
        for i in range(len(all_videos)):
            title_list.append(all_videos[i].title)
            video_id_list.append(all_videos[i].video_id)
        if video_id in video_id_list:
            for i in range(len(all_videos)):
                if all_videos[i].video_id == video_id:
                    to_be_played = all_videos[i].title
                    if VideoPlayer.prev_played in title_list and VideoPlayer.paused not in title_list:
                        print('Stopping video:', VideoPlayer.prev_played)
                        print('Playing video:', to_be_played)
                    if VideoPlayer.paused in title_list:
                        print('Stopping video:', VideoPlayer.paused)
                        print('Playing video:', to_be_played)
                        VideoPlayer.paused=''
                    else:
                        print('Playing video:', to_be_played)
                    VideoPlayer.prev_played=to_be_played
        else:
            print('Cannot play video: Video does not exist')

    def stop_video(self):
        """Stops the current video."""
        all_videos = self._video_library.get_all_videos()
        title_list = []
        for i in range(len(all_videos)):
            title_list.append(all_videos[i].title)
        if VideoPlayer.prev_played in title_list:
            print("Stopping video:", VideoPlayer.prev_played)
            VideoPlayer.prev_played=''
        elif VideoPlayer.prev_played =='':
            print('Cannot stop video: No video is currently playing')


    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        title_list=[]
        for i in range(len(all_videos)):
            title_list.append(all_videos[i].title)
        i = random.randint(0,4)
        random_video = all_videos[i].title
        if VideoPlayer.prev_played in title_list:
            print("Stopping video:", VideoPlayer.prev_played)
            print('Playing video:', random_video)
        elif VideoPlayer.prev_played == '':
            print("Playing video:", random_video)
        VideoPlayer.prev_played = random_video

    def pause_video(self):
        """Pauses the current video."""
        all_videos = self._video_library.get_all_videos()
        title_list = []
        for i in range(len(all_videos)):
            title_list.append(all_videos[i].title)
        if VideoPlayer.paused in title_list:
            print('Video already paused:', VideoPlayer.paused)
        elif VideoPlayer.prev_played in title_list:
            print("Pausing video:", VideoPlayer.prev_played)
            VideoPlayer.paused=VideoPlayer.prev_played
        if VideoPlayer.prev_played =='':
            print('Cannot pause video: No video is currently playing')

    def continue_video(self):
        """Resumes playing the current video."""
        all_videos = self._video_library.get_all_videos()
        title_list = []
        for i in range(len(all_videos)):
            title_list.append(all_videos[i].title)
        if VideoPlayer.paused == '' and VideoPlayer.prev_played in title_list:
            print('Cannot continue video: Video is not paused')
        if VideoPlayer.paused in title_list:
            print('Continuing video:', VideoPlayer.paused)
            VideoPlayer.paused=''
        if VideoPlayer.prev_played =='':
            print('Cannot continue video: No video is currently playing')

    def show_playing(self):
        """Displays video currently playing."""
        all_videos = self._video_library.get_all_videos()
        title_list = []
        for i in range(len(all_videos)):
            title_list.append(all_videos[i].title)

        for i in range(len(all_videos)):
            if VideoPlayer.prev_played == title_list[i]:
                tags = all_videos[i].tags
                if VideoPlayer.prev_played in title_list and VideoPlayer.paused not in title_list:
                    print(f"Currently playing: {VideoPlayer.prev_played} ({all_videos[i].video_id}) [{' '.join(tags)}]")
                elif VideoPlayer.prev_played in title_list and VideoPlayer.paused in title_list:
                    print(f"Currently playing: {VideoPlayer.prev_played} ({all_videos[i].video_id}) [{' '.join(tags)}] - PAUSED")
        if VideoPlayer.prev_played =='':
            print('No video is currently playing')


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        uppercase_playlist_list = [x.upper() for x in VideoPlayer.playlist_list]
        if playlist_name.upper() not in uppercase_playlist_list:
            print('Successfully created new playlist:', playlist_name)
            VideoPlayer.playlist_list.append(playlist_name)
            VideoPlayer.Video_in_playlist_list.append([])
        else:
            print('Cannot create playlist: A playlist with the same name already exists')

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        all_videos = self._video_library.get_all_videos()
        title_list=[]
        video_id_list=[]
        for i in range(len(all_videos)):
            title_list.append(all_videos[i].title)
            video_id_list.append(all_videos[i].video_id)
        uppercase_playlist_list = [x.upper() for x in VideoPlayer.playlist_list]
        if playlist_name.upper() in uppercase_playlist_list:
            for i in range(len(VideoPlayer.playlist_list)):
                if uppercase_playlist_list[i] == playlist_name.upper():
                    for x in range(len(all_videos)):
                        if video_id == video_id_list[x]:
                            video_to_be_added = title_list[x]
                            if video_to_be_added not in VideoPlayer.Video_in_playlist_list[i]:
                                print('Added video to', playlist_name, ': ', video_to_be_added)
                                VideoPlayer.Video_in_playlist_list[i].append(video_to_be_added)
                            elif video_to_be_added in VideoPlayer.Video_in_playlist_list[i]:
                                print('Cannot add video to', playlist_name, ': Video already added')
                    if video_id not in video_id_list:
                        print('Cannot add video to', playlist_name,': Video does not exist')

        if playlist_name.upper() not in uppercase_playlist_list:
            print('Cannot add video to',playlist_name, ': Playlist does not exist')

    def show_all_playlists(self):
        """Display all playlists."""
        if VideoPlayer.playlist_list != []:
            for i in range(len(VideoPlayer.playlist_list)):
                print('Showing all playlists:')
                print("\n".join(VideoPlayer.playlist_list))
        else:
            print('No playlists exist yet')

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name."""
        all_videos = self._video_library.get_all_videos()
        all_video_list = []
        title_list=[]
        print_list=[]
        for i in range(len(all_videos)):
            tags = all_videos[i].tags
            video_id = all_videos[i].video_id
            title = all_videos[i].title
            title_list.append(all_videos[i].title)
            all_video_list.append(f" {title} ({video_id}) [{' '.join(tags)}]")
        uppercase_playlist_list = [x.upper() for x in VideoPlayer.playlist_list]
        if playlist_name.upper() in uppercase_playlist_list:
            for i in range(len(VideoPlayer.playlist_list)):
                if uppercase_playlist_list[i] == playlist_name.upper():
                    if len(VideoPlayer.Video_in_playlist_list[i]) == 0:
                        print('Showing playlist:', playlist_name)
                        print('No videos here yet')
                    else:
                        print('Showing playlist:', playlist_name)
                        print(VideoPlayer.Video_in_playlist_list[i])
                        print(title_list)
                        for a in range(len(VideoPlayer.Video_in_playlist_list[i])):
                            if VideoPlayer.Video_in_playlist_list[a] in title_list:
                                print('1')
                                for b in range(len(title_list)):
                                    if VideoPlayer.Video_in_playlist_list[a] == title_list[b]:
                                        print('2')
                                        print_list.append(all_video_list[b])
                                        print("\n". join(print_list))
            if playlist_name.upper() not in uppercase_playlist_list:
                print('Cannot show playlist', playlist_name, ': Playlist does not exist')

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
