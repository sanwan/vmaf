dataset_name = 'NFLX_public'
yuv_fmt = 'yuv420p'
width = 1920
height = 1080

ref_dir = '[path to dataset videos]/ref'
dis_dir = '[path to dataset videos]/dis'

ref_videos = [
 {'content_id': 0,
  'content_name': 'BigBuckBunny',
  'path': ref_dir + '/BigBuckBunny_25fps.yuv'},
 {'content_id': 1,
  'content_name': 'BirdsInCage',
  'path': ref_dir + '/BirdsInCage_30fps.yuv'},
 {'content_id': 2,
  'content_name': 'CrowdRun',
  'path': ref_dir + '/CrowdRun_25fps.yuv'},
 {'content_id': 3,
  'content_name': 'ElFuente1',
  'path': ref_dir + '/ElFuente1_30fps.yuv'},
 {'content_id': 4,
  'content_name': 'ElFuente2',
  'path': ref_dir + '/ElFuente2_30fps.yuv'},
 {'content_id': 5,
  'content_name': 'FoxBird',
  'path': ref_dir + '/FoxBird_25fps.yuv'},
 {'content_id': 6,
  'content_name': 'OldTownCross',
  'path': ref_dir + '/OldTownCross_25fps.yuv'},
 {'content_id': 7,
  'content_name': 'Seeking',
  'path': ref_dir + '/Seeking_25fps.yuv'},
 {'content_id': 8,
  'content_name': 'Tennis',
  'path': ref_dir + '/Tennis_24fps.yuv'}
]

dis_videos = [{'asset_id': 0,
  'content_id': 0,
  'os': [5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0],
  'path': ref_dir + '/BigBuckBunny_25fps.yuv'},
 {'asset_id': 1,
  'content_id': 1,
  'os': [4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0],
  'path': ref_dir + '/BirdsInCage_30fps.yuv'},
 {'asset_id': 2,
  'content_id': 2,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         3.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0],
  'path': ref_dir + '/CrowdRun_25fps.yuv'},
 {'asset_id': 3,
  'content_id': 3,
  'os': [4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0],
  'path': ref_dir + '/ElFuente1_30fps.yuv'},
 {'asset_id': 4,
  'content_id': 4,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0],
  'path': ref_dir + '/ElFuente2_30fps.yuv'},
 {'asset_id': 5,
  'content_id': 5,
  'os': [4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0],
  'path': ref_dir + '/FoxBird_25fps.yuv'},
 {'asset_id': 6,
  'content_id': 6,
  'os': [3.0,
         5.0,
         4.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         4.0,
         3.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0],
  'path': ref_dir + '/OldTownCross_25fps.yuv'},
 {'asset_id': 7,
  'content_id': 7,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0],
  'path': ref_dir + '/Seeking_25fps.yuv'},
 {'asset_id': 8,
  'content_id': 8,
  'os': [5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0],
  'path': ref_dir + '/Tennis_24fps.yuv'},
 {'asset_id': 9,
  'content_id': 0,
  'os': [1.0,
         1.0,
         1.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         3.0,
         1.0,
         2.0,
         2.0,
         1.0,
         1.0,
         1.0,
         2.0,
         1.0,
         1.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         2.0],
  'path': dis_dir + '/BigBuckBunny_20_288_375.yuv'},
 {'asset_id': 10,
  'content_id': 0,
  'os': [2.0,
         1.0,
         2.0,
         3.0,
         3.0,
         1.0,
         2.0,
         2.0,
         2.0,
         3.0,
         2.0,
         3.0,
         4.0,
         2.0,
         1.0,
         2.0,
         2.0,
         1.0,
         2.0,
         2.0,
         3.0,
         1.0,
         1.0,
         2.0,
         3.0,
         2.0],
  'path': dis_dir + '/BigBuckBunny_30_384_550.yuv'},
 {'asset_id': 11,
  'content_id': 0,
  'os': [2.0,
         2.0,
         2.0,
         3.0,
         2.0,
         2.0,
         2.0,
         2.0,
         2.0,
         4.0,
         3.0,
         3.0,
         3.0,
         5.0,
         2.0,
         2.0,
         2.0,
         4.0,
         2.0,
         2.0,
         2.0,
         2.0,
         2.0,
         1.0,
         3.0,
         3.0],
  'path': dis_dir + '/BigBuckBunny_40_384_750.yuv'},
 {'asset_id': 12,
  'content_id': 0,
  'os': [3.0,
         3.0,
         4.0,
         4.0,
         4.0,
         3.0,
         3.0,
         3.0,
         3.0,
         5.0,
         3.0,
         4.0,
         4.0,
         3.0,
         2.0,
         2.0,
         3.0,
         3.0,
         3.0,
         3.0,
         3.0,
         2.0,
         3.0,
         2.0,
         4.0,
         3.0],
  'path': dis_dir + '/BigBuckBunny_50_480_1050.yuv'},
 {'asset_id': 13,
  'content_id': 0,
  'os': [4.0,
         3.0,
         5.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         4.0,
         2.0,
         4.0,
         5.0],
  'path': dis_dir + '/BigBuckBunny_55_480_1750.yuv'},
 {'asset_id': 14,
  'content_id': 0,
  'os': [5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         3.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0],
  'path': dis_dir + '/BigBuckBunny_75_720_3050.yuv'},
 {'asset_id': 15,
  'content_id': 0,
  'os': [5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         4.0,
         5.0,
         3.0,
         4.0,
         4.0],
  'path': dis_dir + '/BigBuckBunny_80_720_4250.yuv'},
 {'asset_id': 16,
  'content_id': 0,
  'os': [5.0,
         4.0,
         3.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         3.0,
         5.0,
         5.0],
  'path': dis_dir + '/BigBuckBunny_85_1080_3800.yuv'},
 {'asset_id': 17,
  'content_id': 0,
  'os': [5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0],
  'path': dis_dir + '/BigBuckBunny_90_1080_4300.yuv'},
 {'asset_id': 18,
  'content_id': 0,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0],
  'path': dis_dir + '/BigBuckBunny_95_1080_5800.yuv'},
 {'asset_id': 19,
  'content_id': 1,
  'os': [2.0,
         1.0,
         3.0,
         3.0,
         2.0,
         2.0,
         2.0,
         3.0,
         1.0,
         3.0,
         3.0,
         2.0,
         3.0,
         5.0,
         1.0,
         1.0,
         2.0,
         2.0,
         2.0,
         2.0,
         1.0,
         2.0,
         1.0,
         1.0,
         3.0,
         2.0],
  'path': dis_dir + '/BirdsInCage_40_288_375.yuv'},
 {'asset_id': 20,
  'content_id': 1,
  'os': [1.0,
         1.0,
         3.0,
         3.0,
         2.0,
         1.0,
         2.0,
         2.0,
         1.0,
         3.0,
         2.0,
         2.0,
         4.0,
         2.0,
         3.0,
         1.0,
         2.0,
         2.0,
         1.0,
         3.0,
         2.0,
         2.0,
         1.0,
         1.0,
         2.0,
         2.0],
  'path': dis_dir + '/BirdsInCage_50_288_550.yuv'},
 {'asset_id': 21,
  'content_id': 1,
  'os': [2.0,
         2.0,
         4.0,
         3.0,
         1.0,
         3.0,
         2.0,
         3.0,
         3.0,
         4.0,
         2.0,
         3.0,
         4.0,
         3.0,
         3.0,
         1.0,
         2.0,
         2.0,
         2.0,
         3.0,
         3.0,
         3.0,
         2.0,
         2.0,
         3.0,
         4.0],
  'path': dis_dir + '/BirdsInCage_60_384_550.yuv'},
 {'asset_id': 22,
  'content_id': 1,
  'os': [2.0,
         2.0,
         4.0,
         3.0,
         3.0,
         2.0,
         3.0,
         3.0,
         3.0,
         5.0,
         3.0,
         3.0,
         4.0,
         2.0,
         3.0,
         2.0,
         3.0,
         3.0,
         2.0,
         3.0,
         2.0,
         3.0,
         2.0,
         2.0,
         4.0,
         2.0],
  'path': dis_dir + '/BirdsInCage_65_384_750.yuv'},
 {'asset_id': 23,
  'content_id': 1,
  'os': [3.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         3.0,
         3.0,
         5.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         4.0,
         3.0,
         4.0,
         3.0],
  'path': dis_dir + '/BirdsInCage_80_480_750.yuv'},
 {'asset_id': 24,
  'content_id': 1,
  'os': [4.0,
         4.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         4.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         3.0,
         4.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0],
  'path': dis_dir + '/BirdsInCage_85_720_1050.yuv'},
 {'asset_id': 25,
  'content_id': 1,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0],
  'path': dis_dir + '/BirdsInCage_90_1080_1800.yuv'},
 {'asset_id': 26,
  'content_id': 1,
  'os': [4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0],
  'path': dis_dir + '/BirdsInCage_95_1080_3000.yuv'},
 {'asset_id': 27,
  'content_id': 2,
  'os': [1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0],
  'path': dis_dir + '/CrowdRun_03_288_375.yuv'},
 {'asset_id': 28,
  'content_id': 2,
  'os': [2.0,
         2.0,
         2.0,
         2.0,
         2.0,
         1.0,
         2.0,
         3.0,
         1.0,
         3.0,
         1.0,
         3.0,
         1.0,
         2.0,
         2.0,
         2.0,
         2.0,
         2.0,
         2.0,
         2.0,
         1.0,
         2.0,
         2.0,
         1.0,
         3.0,
         2.0],
  'path': dis_dir + '/CrowdRun_40_480_2350.yuv'},
 {'asset_id': 29,
  'content_id': 2,
  'os': [2.0,
         3.0,
         3.0,
         5.0,
         3.0,
         3.0,
         1.0,
         3.0,
         1.0,
         4.0,
         3.0,
         4.0,
         3.0,
         4.0,
         3.0,
         3.0,
         3.0,
         2.0,
         1.0,
         2.0,
         2.0,
         3.0,
         3.0,
         2.0,
         3.0,
         3.0],
  'path': dis_dir + '/CrowdRun_50_1080_4300.yuv'},
 {'asset_id': 30,
  'content_id': 2,
  'os': [3.0,
         3.0,
         4.0,
         3.0,
         4.0,
         3.0,
         3.0,
         4.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         3.0,
         3.0,
         3.0,
         3.0,
         2.0,
         2.0,
         3.0,
         4.0,
         3.0,
         4.0,
         2.0,
         4.0,
         3.0],
  'path': dis_dir + '/CrowdRun_65_1080_5800.yuv'},
 {'asset_id': 31,
  'content_id': 2,
  'os': [3.0,
         3.0,
         5.0,
         5.0,
         4.0,
         5.0,
         3.0,
         5.0,
         4.0,
         5.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         4.0,
         3.0,
         2.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         5.0,
         3.0],
  'path': dis_dir + '/CrowdRun_75_1080_7500.yuv'},
 {'asset_id': 32,
  'content_id': 2,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         3.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         4.0],
  'path': dis_dir + '/CrowdRun_80_1080_10000.yuv'},
 {'asset_id': 33,
  'content_id': 2,
  'os': [5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0],
  'path': dis_dir + '/CrowdRun_90_1080_15000.yuv'},
 {'asset_id': 34,
  'content_id': 3,
  'os': [1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         3.0,
         1.0,
         1.0,
         2.0,
         2.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0],
  'path': dis_dir + '/ElFuente1_10_288_375.yuv'},
 {'asset_id': 35,
  'content_id': 3,
  'os': [1.0,
         1.0,
         2.0,
         2.0,
         3.0,
         1.0,
         1.0,
         1.0,
         1.0,
         2.0,
         3.0,
         3.0,
         3.0,
         2.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         2.0],
  'path': dis_dir + '/ElFuente1_25_384_750.yuv'},
 {'asset_id': 36,
  'content_id': 3,
  'os': [3.0,
         3.0,
         4.0,
         5.0,
         4.0,
         4.0,
         3.0,
         4.0,
         2.0,
         4.0,
         4.0,
         3.0,
         4.0,
         3.0,
         2.0,
         3.0,
         3.0,
         2.0,
         3.0,
         3.0,
         2.0,
         3.0,
         2.0,
         2.0,
         4.0,
         3.0],
  'path': dis_dir + '/ElFuente1_50_480_1750.yuv'},
 {'asset_id': 37,
  'content_id': 3,
  'os': [2.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         3.0,
         3.0,
         3.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         3.0,
         4.0,
         4.0],
  'path': dis_dir + '/ElFuente1_60_720_2350.yuv'},
 {'asset_id': 38,
  'content_id': 3,
  'os': [4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         3.0,
         5.0,
         5.0,
         4.0,
         3.0,
         4.0,
         3.0,
         4.0,
         3.0,
         4.0,
         3.0,
         5.0,
         4.0],
  'path': dis_dir + '/ElFuente1_70_1080_4300.yuv'},
 {'asset_id': 39,
  'content_id': 3,
  'os': [4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0],
  'path': dis_dir + '/ElFuente1_85_1080_5800.yuv'},
 {'asset_id': 40,
  'content_id': 3,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0],
  'path': dis_dir + '/ElFuente1_90_1080_7500.yuv'},
 {'asset_id': 41,
  'content_id': 4,
  'os': [1.0,
         1.0,
         3.0,
         1.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         4.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         2.0,
         1.0],
  'path': dis_dir + '/ElFuente2_05_288_375.yuv'},
 {'asset_id': 42,
  'content_id': 4,
  'os': [1.0,
         2.0,
         3.0,
         2.0,
         4.0,
         2.0,
         3.0,
         2.0,
         2.0,
         5.0,
         3.0,
         4.0,
         4.0,
         3.0,
         2.0,
         3.0,
         3.0,
         2.0,
         3.0,
         2.0,
         3.0,
         2.0,
         2.0,
         1.0,
         2.0,
         3.0],
  'path': dis_dir + '/ElFuente2_30_480_1750.yuv'},
 {'asset_id': 43,
  'content_id': 4,
  'os': [2.0,
         1.0,
         2.0,
         3.0,
         5.0,
         4.0,
         2.0,
         3.0,
         4.0,
         4.0,
         3.0,
         4.0,
         4.0,
         3.0,
         2.0,
         4.0,
         3.0,
         2.0,
         2.0,
         2.0,
         4.0,
         2.0,
         2.0,
         2.0,
         3.0,
         4.0],
  'path': dis_dir + '/ElFuente2_50_720_3050.yuv'},
 {'asset_id': 44,
  'content_id': 4,
  'os': [3.0,
         3.0,
         5.0,
         2.0,
         5.0,
         1.0,
         1.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         4.0,
         3.0,
         3.0,
         2.0,
         4.0,
         4.0,
         2.0,
         2.0,
         4.0,
         3.0,
         3.0,
         2.0,
         4.0,
         4.0],
  'path': dis_dir + '/ElFuente2_60_1080_4300.yuv'},
 {'asset_id': 45,
  'content_id': 4,
  'os': [4.0,
         3.0,
         4.0,
         2.0,
         5.0,
         4.0,
         3.0,
         4.0,
         4.0,
         5.0,
         3.0,
         4.0,
         4.0,
         2.0,
         3.0,
         4.0,
         5.0,
         2.0,
         4.0,
         3.0,
         5.0,
         4.0,
         3.0,
         2.0,
         5.0,
         4.0],
  'path': dis_dir + '/ElFuente2_65_720_4250.yuv'},
 {'asset_id': 46,
  'content_id': 4,
  'os': [5.0,
         2.0,
         3.0,
         3.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         3.0,
         3.0,
         4.0,
         4.0,
         3.0,
         4.0,
         2.0,
         5.0,
         4.0],
  'path': dis_dir + '/ElFuente2_70_1080_5800.yuv'},
 {'asset_id': 47,
  'content_id': 4,
  'os': [4.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         2.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         4.0,
         5.0,
         5.0],
  'path': dis_dir + '/ElFuente2_80_1080_10000.yuv'},
 {'asset_id': 48,
  'content_id': 4,
  'os': [5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0],
  'path': dis_dir + '/ElFuente2_85_1080_15000.yuv'},
 {'asset_id': 49,
  'content_id': 4,
  'os': [5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0],
  'path': dis_dir + '/ElFuente2_90_1080_20000.yuv'},
 {'asset_id': 50,
  'content_id': 5,
  'os': [1.0,
         2.0,
         3.0,
         2.0,
         1.0,
         2.0,
         3.0,
         2.0,
         1.0,
         4.0,
         2.0,
         2.0,
         3.0,
         1.0,
         2.0,
         3.0,
         2.0,
         2.0,
         2.0,
         1.0,
         2.0,
         2.0,
         1.0,
         1.0,
         2.0,
         2.0],
  'path': dis_dir + '/FoxBird_20_288_375.yuv'},
 {'asset_id': 51,
  'content_id': 5,
  'os': [3.0,
         2.0,
         5.0,
         2.0,
         4.0,
         3.0,
         3.0,
         2.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         3.0,
         3.0,
         4.0,
         2.0,
         3.0,
         3.0,
         3.0,
         3.0,
         2.0,
         3.0,
         3.0,
         3.0,
         3.0],
  'path': dis_dir + '/FoxBird_40_384_750.yuv'},
 {'asset_id': 52,
  'content_id': 5,
  'os': [4.0,
         3.0,
         4.0,
         4.0,
         3.0,
         4.0,
         3.0,
         4.0,
         4.0,
         4.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         3.0,
         3.0,
         3.0,
         3.0,
         3.0,
         3.0,
         3.0,
         2.0,
         3.0,
         4.0,
         3.0],
  'path': dis_dir + '/FoxBird_55_480_750.yuv'},
 {'asset_id': 53,
  'content_id': 5,
  'os': [4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         4.0,
         4.0,
         5.0,
         3.0,
         4.0,
         5.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         4.0,
         3.0,
         4.0,
         4.0,
         5.0],
  'path': dis_dir + '/FoxBird_65_480_1750.yuv'},
 {'asset_id': 54,
  'content_id': 5,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         3.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         4.0],
  'path': dis_dir + '/FoxBird_80_1080_2300.yuv'},
 {'asset_id': 55,
  'content_id': 5,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0],
  'path': dis_dir + '/FoxBird_95_1080_5800.yuv'},
 {'asset_id': 56,
  'content_id': 6,
  'os': [1.0,
         1.0,
         1.0,
         1.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         2.0,
         1.0],
  'path': dis_dir + '/OldTownCross_20_288_375.yuv'},
 {'asset_id': 57,
  'content_id': 6,
  'os': [1.0,
         2.0,
         3.0,
         2.0,
         2.0,
         1.0,
         4.0,
         2.0,
         1.0,
         3.0,
         1.0,
         2.0,
         2.0,
         1.0,
         2.0,
         1.0,
         2.0,
         1.0,
         1.0,
         2.0,
         2.0,
         1.0,
         2.0,
         2.0,
         3.0,
         2.0],
  'path': dis_dir + '/OldTownCross_45_384_750.yuv'},
 {'asset_id': 58,
  'content_id': 6,
  'os': [3.0,
         2.0,
         3.0,
         4.0,
         3.0,
         2.0,
         3.0,
         3.0,
         1.0,
         4.0,
         3.0,
         3.0,
         2.0,
         2.0,
         3.0,
         2.0,
         2.0,
         2.0,
         2.0,
         1.0,
         3.0,
         2.0,
         2.0,
         2.0,
         3.0,
         2.0],
  'path': dis_dir + '/OldTownCross_55_480_750.yuv'},
 {'asset_id': 59,
  'content_id': 6,
  'os': [3.0,
         3.0,
         2.0,
         3.0,
         4.0,
         4.0,
         5.0,
         4.0,
         3.0,
         5.0,
         2.0,
         3.0,
         4.0,
         3.0,
         2.0,
         2.0,
         2.0,
         2.0,
         3.0,
         3.0,
         3.0,
         3.0,
         3.0,
         2.0,
         4.0,
         3.0],
  'path': dis_dir + '/OldTownCross_60_480_1750.yuv'},
 {'asset_id': 60,
  'content_id': 6,
  'os': [5.0,
         4.0,
         5.0,
         3.0,
         4.0,
         4.0,
         5.0,
         5.0,
         3.0,
         5.0,
         4.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         4.0,
         4.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         4.0],
  'path': dis_dir + '/OldTownCross_80_720_2350.yuv'},
 {'asset_id': 61,
  'content_id': 6,
  'os': [4.0,
         5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         3.0,
         5.0,
         4.0,
         4.0,
         4.0,
         4.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         3.0],
  'path': dis_dir + '/OldTownCross_85_720_2950.yuv'},
 {'asset_id': 62,
  'content_id': 6,
  'os': [5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0],
  'path': dis_dir + '/OldTownCross_90_1080_4300.yuv'},
 {'asset_id': 63,
  'content_id': 7,
  'os': [1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         2.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0,
         1.0],
  'path': dis_dir + '/Seeking_10_288_375.yuv'},
 {'asset_id': 64,
  'content_id': 7,
  'os': [2.0,
         2.0,
         4.0,
         1.0,
         3.0,
         2.0,
         2.0,
         3.0,
         1.0,
         2.0,
         2.0,
         3.0,
         4.0,
         3.0,
         2.0,
         2.0,
         2.0,
         1.0,
         1.0,
         1.0,
         2.0,
         2.0,
         2.0,
         1.0,
         2.0,
         2.0],
  'path': dis_dir + '/Seeking_30_480_1050.yuv'},
 {'asset_id': 65,
  'content_id': 7,
  'os': [2.0,
         2.0,
         3.0,
         2.0,
         4.0,
         1.0,
         3.0,
         4.0,
         2.0,
         4.0,
         3.0,
         4.0,
         3.0,
         3.0,
         3.0,
         3.0,
         2.0,
         2.0,
         2.0,
         3.0,
         2.0,
         2.0,
         3.0,
         1.0,
         3.0,
         3.0],
  'path': dis_dir + '/Seeking_45_480_1750.yuv'},
 {'asset_id': 66,
  'content_id': 7,
  'os': [3.0,
         3.0,
         3.0,
         4.0,
         3.0,
         5.0,
         3.0,
         4.0,
         3.0,
         5.0,
         3.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         4.0,
         2.0,
         2.0,
         4.0,
         3.0,
         3.0,
         2.0,
         2.0,
         3.0,
         4.0],
  'path': dis_dir + '/Seeking_50_720_2350.yuv'},
 {'asset_id': 67,
  'content_id': 7,
  'os': [4.0,
         4.0,
         3.0,
         3.0,
         5.0,
         3.0,
         3.0,
         3.0,
         3.0,
         5.0,
         4.0,
         4.0,
         5.0,
         3.0,
         5.0,
         3.0,
         3.0,
         3.0,
         3.0,
         4.0,
         4.0,
         3.0,
         4.0,
         3.0,
         5.0,
         4.0],
  'path': dis_dir + '/Seeking_60_720_3050.yuv'},
 {'asset_id': 68,
  'content_id': 7,
  'os': [4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         2.0,
         3.0,
         5.0,
         4.0,
         5.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         3.0,
         4.0,
         3.0,
         2.0,
         4.0,
         4.0,
         3.0,
         4.0,
         3.0,
         5.0,
         4.0],
  'path': dis_dir + '/Seeking_65_1080_4300.yuv'},
 {'asset_id': 69,
  'content_id': 7,
  'os': [4.0,
         5.0,
         4.0,
         5.0,
         3.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         3.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         3.0,
         4.0,
         4.0,
         3.0,
         5.0,
         3.0,
         4.0,
         4.0,
         5.0],
  'path': dis_dir + '/Seeking_75_1080_5800.yuv'},
 {'asset_id': 70,
  'content_id': 7,
  'os': [3.0,
         5.0,
         3.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         3.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0],
  'path': dis_dir + '/Seeking_85_1080_7500.yuv'},
 {'asset_id': 71,
  'content_id': 7,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         1.0,
         3.0,
         5.0,
         3.0,
         5.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         3.0,
         5.0,
         4.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0],
  'path': dis_dir + '/Seeking_90_1080_15000.yuv'},
 {'asset_id': 72,
  'content_id': 7,
  'os': [5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         4.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0,
         3.0,
         4.0,
         5.0,
         5.0,
         4.0,
         4.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0],
  'path': dis_dir + '/Seeking_95_1080_20000.yuv'},
 {'asset_id': 73,
  'content_id': 8,
  'os': [2.0,
         1.0,
         2.0,
         2.0,
         1.0,
         1.0,
         1.0,
         3.0,
         1.0,
         3.0,
         1.0,
         1.0,
         2.0,
         1.0,
         1.0,
         1.0,
         2.0,
         2.0,
         2.0,
         2.0,
         1.0,
         2.0,
         1.0,
         1.0,
         3.0,
         1.0],
  'path': dis_dir + '/Tennis_20_288_375.yuv'},
 {'asset_id': 74,
  'content_id': 8,
  'os': [1.0,
         2.0,
         2.0,
         2.0,
         3.0,
         2.0,
         5.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         2.0,
         2.0,
         2.0,
         2.0,
         3.0,
         2.0,
         2.0,
         2.0,
         2.0,
         2.0,
         3.0],
  'path': dis_dir + '/Tennis_40_384_750.yuv'},
 {'asset_id': 75,
  'content_id': 8,
  'os': [3.0,
         2.0,
         4.0,
         4.0,
         3.0,
         3.0,
         2.0,
         4.0,
         3.0,
         4.0,
         4.0,
         4.0,
         4.0,
         4.0,
         3.0,
         2.0,
         2.0,
         4.0,
         2.0,
         4.0,
         3.0,
         2.0,
         3.0,
         3.0,
         5.0,
         3.0],
  'path': dis_dir + '/Tennis_60_480_1050.yuv'},
 {'asset_id': 76,
  'content_id': 8,
  'os': [3.0,
         3.0,
         5.0,
         3.0,
         3.0,
         4.0,
         3.0,
         4.0,
         1.0,
         4.0,
         3.0,
         4.0,
         5.0,
         3.0,
         3.0,
         4.0,
         3.0,
         3.0,
         3.0,
         3.0,
         2.0,
         3.0,
         3.0,
         4.0,
         4.0,
         3.0],
  'path': dis_dir + '/Tennis_70_480_1750.yuv'},
 {'asset_id': 77,
  'content_id': 8,
  'os': [3.0,
         5.0,
         5.0,
         3.0,
         5.0,
         5.0,
         5.0,
         5.0,
         2.0,
         5.0,
         5.0,
         4.0,
         5.0,
         3.0,
         4.0,
         4.0,
         5.0,
         4.0,
         3.0,
         5.0,
         4.0,
         3.0,
         4.0,
         4.0,
         5.0,
         5.0],
  'path': dis_dir + '/Tennis_80_720_3050.yuv'},
 {'asset_id': 78,
  'content_id': 8,
  'os': [5.0,
         5.0,
         4.0,
         3.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         5.0,
         4.0,
         5.0,
         3.0,
         5.0,
         4.0,
         5.0,
         5.0,
         5.0,
         5.0,
         5.0,
         4.0,
         5.0,
         4.0,
         5.0,
         4.0],
  'path': dis_dir + '/Tennis_90_1080_4300.yuv'}]
