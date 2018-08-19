
# angular笔记


## 安装

```shell
npm install -g @angular/cli
```

## 命令工具
```shell
ng new my-app  创建项目

cd my-app
ng serve --open 运行项目

ng build 构建项目（编译）

ng test 测试（karma）

ng generate component aaa  创建组件

ng generate service aaa 创建服务  服务是用来操作数据的（获取数据） 组件则专注于展现数据
```



## 语法
```shell
import { FormsModel} from '@angular/forms';
[(ngModel}]="hero.name"  双向绑定


<li *ngFor="let a of list">  循环
</li>


<li *ngFor="let hero of heroes" (click)="onSelect(hero)"> 事件绑定

<div *ngIf="selectedHero">  条件判断


[class.selected]="hero === selectedHero"  css类绑定

@Input() 父子组件之间的数据传递，定义子组件作为一个元素的属性可以被绑定

```