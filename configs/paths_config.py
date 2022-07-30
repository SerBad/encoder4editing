dataset_paths = {
    #  Face Datasets (In the paper: FFHQ - train, CelebAHQ - test)
    'ffhq': '',
    'celeba_test': '',

    #  Cars Dataset (In the paper: Stanford cars)
    'cars_train': '',
    'cars_test': '',

    #  Horse Dataset (In the paper: LSUN Horse)
    'horse_train': '',
    'horse_test': '',

    #  Church Dataset (In the paper: LSUN Church)
    'church_train': '',
    'church_test': '',

    #  Cats Dataset (In the paper: LSUN Cat)
    'cats_train': '',
    'cats_test': '',

    'train_data': '/kaggle/input/encoder4editing/encoder4editing/data/head2/images/train',
    'test_data': '/kaggle/input/encoder4editing/encoder4editing/data/head2/images/test',
}

model_paths = {
    'stylegan_ffhq': '/kaggle/input/encoder4editing/encoder4editing/pretrained_models/stylegan2-ffhq-config-f.pt',
    'ir_se50': '/kaggle/input/encoder4editing/encoder4editing/pretrained_models/model_ir_se50.pth',
    'shape_predictor': '/kaggle/input/encoder4editing/encoder4editing/pretrained_models/shape_predictor_68_face_landmarks.dat',
    'moco': '/kaggle/input/encoder4editing/encoder4editing/pretrained_models/moco_v2_800ep_pretrain.pt'
}
