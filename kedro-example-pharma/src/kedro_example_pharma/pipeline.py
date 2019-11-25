# Copyright 2018-2019 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
#     or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.
"""Pipeline construction."""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.decorators import log_time
from kedro_example_pharma.nodes.data_engineering import (
    preprocess_observations,
    preprocess_diagnosis,
)

from kedro_example_pharma.nodes.price_prediction import (
    split_data,
    train_cox_ph_model,
    evaluate_model,
)


# Here you can define your data-driven pipeline by importing your functions
# and adding them to the pipeline as follows:
#
# from nodes.data_wrangling import clean_data, compute_features
#
# pipeline = Pipeline([
#     node(clean_data, 'customers', 'prepared_customers'),
#     node(compute_features, 'prepared_customers', ['X_train', 'Y_train'])
# ])
#
# Once you have your pipeline defined, you can run it from the root of your
# project by calling:
#
# $ kedro run
#

def pass_through(*vargs, **kwargs):
    return None


def preprocess_labs(*vargs, **kwargs):
    return None


def combine_lab_values_and_ranges(*vargs, **kwargs):
    pass


def transform_observations(*vargs, **kwargs):
    pass


def create_endpoint_stomach_cancer(*vargs, **kwargs):
    return None


def create_demographics(*vargs, **kwargs):
    return None


def create_model_input_stomach_cancer(*vargs, **kwargs):
    return None


def create_pipeline(**kwargs):
    """Create the project's pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        Pipeline: The resulting pipeline.

    """
    de_pipeline = Pipeline(
        [
            node(
                preprocess_observations,
                "raw: observations",
                "int: typed_observations",
                tags=["observations", "1 - raw"]
            ),
            node(
                preprocess_diagnosis,
                "raw: diagnosis",
                "int: typed_diagnosis",
                tags=["diagnosis", "1 - raw"]
            ),
            node(
                preprocess_labs,
                "raw: lab_values",
                "int: typed_lab_values",
                tags=["labs", "1 - raw"]
            ),
            node(
                preprocess_labs,
                "raw: lab_ranges",
                "int: typed_lab_ranges",
                tags=["labs", "1 - raw"]
            ),
            node(
                pass_through,
                "raw: patients",
                "int: patients",
                tags=["patients", "1 - raw"]
            ),
            node(
                pass_through,
                "int: patients",
                "prm: patients",
                tags=["patients", "2 - intermediate"]
            ),
            node(
                transform_observations,
                "int: typed_observations",
                "prm: patient_indexed_observations",
                tags=["observations", "2 - intermediate"]
            ),
            node(
                pass_through,
                "int: typed_diagnosis",
                "prm: diagnosis",
                tags=["diagnosis", "2 - intermediate"]
            ),
            node(
                combine_lab_values_and_ranges,
                ["int: typed_lab_ranges", "int: typed_lab_values"],
                "prm: labs",
                tags=["labs", "2 - intermediate"]
            ),
            node(
                create_endpoint_stomach_cancer,
                ["prm: patient_indexed_observations", "prm: diagnosis", "prm: labs"],
                "fea: endpoint_stomach_cancer",
                tags=["3 - primary", "endpoints"]

            ),
            node(
                create_demographics,
                ["prm: patients"],
                "fea: demographics",
                tags=["3 - primary", "features"]
            ),
            node(
                create_model_input_stomach_cancer,
                ["fea: endpoint_stomach_cancer", "fea: demographics"],
                "inp: cancer_incidence",
                tags=["4 - feature"]

            ),
        ],
        tags=["de"]
    ).decorate(log_time)

    ds_pipeline = Pipeline(
        [
            node(
                split_data,
                ["inp: cancer_incidence", "param: train_split_proportion"],
                ["X_train", "X_test", "y_train", "y_test"],
                tags=["5 - model input"]
            ),
            node(
                train_cox_ph_model,
                ["X_train", "y_train"],
                "model_cancer_proportional_hazards"
            ),
            node(
                evaluate_model,
                ["model_cancer_proportional_hazards", "X_test", "y_test"],
                None
            ),
        ],
        tags=["ds"],
    ).decorate(log_time)

    return de_pipeline + ds_pipeline
