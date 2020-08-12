<template>
  <div>
    <div>
      <el-carousel :interval="4000" type="card" height="400px">
        <el-carousel-item v-for="(item, index) in params" :key="index">
          <img :src="item.url" width="800" :title="item.name" />
        </el-carousel-item>
      </el-carousel>
    </div>
    <div>
      <el-button
        type="primary"
        @click="(drawer = true), (add = true), (del = false), (update = false)"
        >添加幻灯片</el-button
      >
      <el-button
        type="danger"
        @click="(drawer = true), (del = true), (add = false), (update = false)"
        >删除幻灯片</el-button
      >
    </div>
    <div>
      <el-drawer :visible.sync="drawer" :with-header="false">
        <el-input
          placeholder="请输入幻灯片名称"
          v-model="name"
          clearable
          v-show="add"
        ></el-input
        ><br /><br />
        <el-input
          placeholder="请输入幻灯片url"
          v-model="url"
          v-show="add"
          clearable
        ></el-input>
        <!-- 幻灯片信息表格--删除 -->
        <el-table :data="params" style="width: 100%" v-show="del">
          <el-table-column prop="name" label="名称" width="100">
          </el-table-column>
          <el-table-column prop="url" label="路由" width="180">
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button type="text" @click="del_pics(scope.row)"
                >删除</el-button
              >
            </template>
          </el-table-column>
        </el-table>
        <br /><br />
        <el-button type="primary" v-show="add" @click="add_pics"
          >确认添加</el-button
        >
      </el-drawer>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      // 幻灯片数据
      params: [],
      // 抽屉打开关闭
      drawer: false,
      // 新增幻灯片的name
      name: "",
      // 新增幻灯片url
      url: "",
      // 添加按钮
      add: false,
      // 删除按钮
      del: false
    };
  },
  methods: {
    // 获取幻灯片列表
    get_pics: function() {
      this.axios({
        url: "http://localhost:8000/carousel/"
      }).then(res => {
        if (res.data.code == 405) {
          this.$message(res.data.msg);
        } else {
          this.params = res.data.pics;
        }
      });
    },
    // 添加幻灯片方法
    add_pics: function() {
      if (this.name) {
        if (this.url) {
          this.axios({
            url: "http://localhost:8000/carousel/",
            method: "post",
            data: {
              name: this.name,
              url: this.url
            }
          }).then(res => {
            this.$message(res.data.msg);
            this.name = "";
            this.url = "";
            if ((res.data.msg = "添加成功")) {
              this.get_pics();
            }
          });
        } else {
          this.$message("未输入幻灯片url");
        }
      } else {
        this.$message("未输入幻灯片名称");
      }
    },
    // 删除幻灯片方法
    del_pics(row) {
      this.axios({
        url: "http://localhost:8000/carousel/",
        method: "delete",
        data: {
          pid: row.id
        }
      }).then(res => {
        this.$message(res.data.msg);
        this.get_pics();
      });
    }
  },
  mounted: function() {
    this.get_pics();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
