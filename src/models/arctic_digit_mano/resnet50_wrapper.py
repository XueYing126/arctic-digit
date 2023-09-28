from src.callbacks.loss.loss_arctic_digit_mano import compute_loss
from src.callbacks.process.process_arctic import process_data
from src.callbacks.vis.visualize_arctic import visualize_all
from src.models.arctic_digit_mano.model import ArcticDigitMano
from src.models.generic.wrapper import GenericWrapper


class ArcticDigitManoWrapper(GenericWrapper):
    def __init__(self, args):
        super().__init__(args)
        self.model = ArcticDigitMano(
            backbone="resnet50", # hrnet, resnet50
            focal_length=args.focal_length,
            img_res=args.img_res,
            args=args,
        )
        self.process_fn = process_data
        self.loss_fn = compute_loss
        self.metric_dict = [
            "cdev",
            "mrrpe",
            "mpjpe.ra",
            "aae",
            "success_rate",
        ]

        self.vis_fns = [visualize_all]

        self.num_vis_train = 1
        self.num_vis_val = 1

    def inference(self, inputs, meta_info):
        return super().inference_pose(inputs, meta_info)