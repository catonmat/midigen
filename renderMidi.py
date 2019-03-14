from mido import Message, MidiFile, MidiTrack
import midigen as mg

mid = MidiFile(type=1)
dyad_track = MidiTrack()
mid.tracks.append(dyad_track)
arp_track = MidiTrack()
mid.tracks.append(arp_track)


spectral_array = mg.create_spectral_array(3300, 5100, 4)
mg.make_spectral_arpeggio_midi(mid, spectral_array, 100, 4)

for i, track in enumerate(mid.tracks):
	print('Track {}: {}'.format(i, track.name))
	for msg in track:
		print(msg)
	print("break")
	mg.flatten_midi_channels(track)
	mg.cycle_midi_channels(track, 2)
	for msg in track:
		print(msg)

#mid.save('output/song8.mid')