from deep_sort_realtime.deepsort_tracker import DeepSort


tracker = DeepSort()


tracks = tracker.update_tracks(


detections


)


for track in tracks:


    if not track.is_confirmed():

        continue


    print(track.track_id)