# Integrate the Inference Engine in An Edge App

You've come a long way from the first lesson where most of the code for working with
the OpenVINO toolkit was happening in the background. You worked with pre-trained models,
moved up to converting any trained model to an Intermediate Representation with the
Model Optimizer, and even got the model loaded into the Inference Engine and began making
inference requests.

In this final exercise of this lesson, you'll close off the OpenVINO workflow by extracting
the results of the inference request, and then integrating the Inference Engine into an existing
application. You'll still be given some of the overall application infrastructure, as more that of
will come in the next lesson, but all of that is outside of OpenVINO itself.

You will also add code allowing you to try out various confidence thresholds with the model,
as well as changing the visual look of the output, like bounding box colors.

Now, it's up to you which exact model you want to use here, although you are able to just
re-use the model you converted with TensorFlow before for an easy bounding box dectector.

Note that this application will run with a video instead of just images like we've done before.

So, your tasks are to:

1. Convert a bounding box model to an IR with the Model Optimizer.
2. Pre-process the model as necessary.
3. Use an async request to perform inference on each video frame.
4. Extract the results from the inference request.
5. Add code to make the requests and feed back the results within the application.
6. Perform any necessary post-processing steps to get the bounding boxes.
7. Add a command line argument to allow for different confidence thresholds for the model.
8. Add a command line argument to allow for different bounding box colors for the output.
9. Correctly utilize the command line arguments in #3 and #4 within the application.

When you are done, feed your model to `app.py`, and it will generate `out.mp4`, which you
can download and view. *Note that this app will take a little bit longer to run.* Also, if you need
to re-run inference, delete the `out.mp4` file first.

You only need to feed the model with `-m` before adding the customization; you should set
defaults for any additional arguments you add for the color and confidence so that the user
does not always need to specify them.

```bash
python app.py -m {your-model-path.xml}
```
