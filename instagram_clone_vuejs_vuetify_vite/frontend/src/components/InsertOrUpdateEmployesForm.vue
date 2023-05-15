<template>
  <vee-form :validation-schema="loginSchema" @submit="loginAuth" class="veeform">

              <v-row v-if="type == 'Employes'">
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    label='Legal first name*'
                    v-model="firstNameInsert"
                    clearable
                    hide-details="auto"
                    hint="enter first name"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    label="Legal middle name"
                    v-model="middleNameInsert"
                    clearable
                    hide-details="auto"
                    hint="enter middle name"
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    label="Legal last name*"
                    :v-model="legalLastName"
                    clearable
                    hide-details="auto"
                    hint="enter last name"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Email*"
                    :v-model="Email"
                    placeholder="johndoe@gmail.com"
                    hint="enter email"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Password*"
                    :v-model="Password"
                    hint="enter password"
                    type="password"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                >
                  <v-select
                    :items="['0-17', '18-29', '30-54', '54+']"
                    :v-model="Age"
                    label="Age*"
                    hint="enter age"
                    required
                  ></v-select>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                >
                  <v-autocomplete
                    :items="['Administration', 'Driver', 'Engineer', 'Cleaner', 'Manager']"
                    :v-model="Position"
                    label="Position"
                    hint="enter working position"
                    multiple
                  ></v-autocomplete>
                </v-col>
              </v-row>
              <v-row v-else-if="type == 'Containers'">
                <v-col cols="12" sm="6" md="4">
                  <div class="field">
                      <vee-field type="email" name="email" class="veeinput" placeholder="Email*" />
                  </div>
                  <ErrorMessage style="color:red;" name="email" />  
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <div class="field">
                      <vee-field type="password" name="password" autocomplete="on" class="veeinput" placeholder="Password*" />
                  </div>
                  <ErrorMessage style="color:red;" name="password" />
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <div class="field">
                    <vee-field type="country" name="country" autocomplete="on" class="veeinput" placeholder="Country*" />
                  </div>
                  <ErrorMessage style="color:red;" name="country" />
                </v-col>
                <v-col cols="12">
                  <div class="field">
                    <vee-field type="responsibleName" name="responsibleName" autocomplete="on" class="veeinput" placeholder="Responsible Name" />
                  </div>
                  <ErrorMessage style="color:red;" name="responsibleName" />
                </v-col>
                <v-col cols="12">
                  <div class="field">
                    <vee-field type="clientName" name="clientName" autocomplete="on" class="veeinput" placeholder="Client Name"/>
                  </div>
                  <ErrorMessage style="color:red;" name="clientName" />
                </v-col>
                <v-col cols="12" sm="6">
                  <v-select
                    label="Transport Type"
                    v-model="Transport"
                    :items="['Air', 'Land', 'Sea']"
                    class="mt-4"
                    hide-details
                  ></v-select>
                  <span v-if="submitClicked && !Transport.length" style="color:red;">{{TransportAlarm}}</span>
                </v-col>
                <v-col cols="12" sm="6" >
                  <v-autocomplete
                    :items="['Oil', 'Cooking Oil', 'Greese', 'Cleaning liquid']"
                    label="Product Type"
                    v-model="ProductType"
                    hint="enter type of the product"
                    class="mt-4"
                    multiple
                    hide-details
                  ></v-autocomplete>
                  <span v-if="submitClicked && !ProductType.length" style="color:red;">{{ProductTypeAlarm}}</span>
                </v-col>
              </v-row>
              <v-btn 
              type="submit" 
              block 
              class="mt-10 submit"
              @click="insertOrUpdateItem"
              :disabled="login_in_submission"
              >
              Submit</v-btn>
                  </vee-form>


                  <br>
                  <div v-if="login_show_alert" :style="login_alert_variant" style="text-align:center;">
                    {{ login_alert_msg }}
                  </div>
</template>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');

.text{
  font-size: 30px;
  color: white;
  font-weight: 600;
  letter-spacing: 2px;
  // text-align:center;
}
// .veeform{
//   margin-top: 10px;
// }
.veeform .field{
  margin-top: 20px;
  display: flex;
}
.field .fas{
  height: 50px;
  width: 60px;
  color: #868686;
  font-size: 20px;
  line-height: 50px;
  border-bottom: 1px solid #444;
  border-right: none;
  border-radius: 5px 0 0 5px;
  background: linear-gradient(#333,#222);
}
.field .veeinput,.veeform button{
  height: 50px;
  width: 100%;
  outline: none;
  font-size: 16px;
  color: #bbb;
  padding: 0 15px;
  border-radius: 0 5px 5px 0;
  border-bottom: 1px solid #bbb;
  caret-color: #3399cc;
  // background: linear-gradient(#333,#222);
  // background: linear-gradient(#bbb, #ddd);
  background: linear-gradient(#F8F8F8	, #F8F8F8);
  // background: linear-gradient(#DDD, #BBB);
  // background: linear-gradient(hsl(0, 0%, 50%), hsl(0, 0%, 30%));




}
.veeinput:focus {
  color: #3399cc;
  box-shadow: 0 0 5px rgba(0, 191, 255, 0.2),
              inset 0 0 5px rgba(0, 191, 255, 0.1);
  // background: linear-gradient(#333933, #222922);
  animation: glow .8s ease-out infinite alternate;
}

@keyframes glow {
  0% {
    border-color: #3399cc;
    // box-shadow: 0 0 5px rgba(0, 191, 255, 0.2),
    //             inset 0 0 5px rgba(0, 0, 0, 0.1);
  }
  100% {
    border-color: #99ccff;
    // box-shadow: 0 0 20px rgba(0, 191, 255, 0.6),
    //             inset 0 0 10px rgba(0, 191, 255, 0.4);
  }
}

.submit{
  margin-top: 30px;
  border-radius: 5px!important;
  font-weight: 600;
  letter-spacing: 1px;
  cursor: pointer;
}
.submit:hover{
  color: #3399cc;
  border: 1px solid #3399cc;
  box-shadow: 0 0 5px rgba(0, 191, 255, 0.3),
              0 0 10px rgba(0, 191, 255, 0.2),
              0 0 15px rgba(0, 191, 255, 0.1);
}

</style>